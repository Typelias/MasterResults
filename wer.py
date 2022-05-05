import matplotlib.pylab as plt
import numpy as np
from utils import getCommandWERForModels, getAvg, getMax, getMin
import pandas as pd
import seaborn as sns


plt.rcParams["patch.force_edgecolor"] = True

models_fetch = ['silero', 'brain', 's2t', 'ws']
models = ['Silero STT', 'SpeechBrain wav2vec2', 'Facebook Speech2Text', 'WebSpeech API']


for i in range(10):
    model_mean = getCommandWERForModels(models_fetch, getAvg, i)

    df = pd.DataFrame({'Models': models, 'Average WER (%)': model_mean})

    model_min = getCommandWERForModels(models_fetch, getMin, i)
    model_max = getCommandWERForModels(models_fetch, getMax, i)

    #print(df)

    error = {}

    for j in range(4):
        error[model_mean[j]] = {'min': model_min[j], 'max': model_max[j]}

    #print(error)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='Models', y='Average WER (%)', data=df, ax=ax)

    for p in ax.patches: 
        x = p.get_x()
        w = p.get_width()
        h = p.get_height()
        min_y = error[h]['min']
        max_y = error[h]['max']
        plt.vlines(x + w/2, min_y, max_y, color='k')

        lineWidth = 0.2
        plt.hlines(max_y, x+lineWidth, x + w - lineWidth, color='k')
        plt.hlines(min_y, x + lineWidth, x + w - lineWidth, color='k')

    plt.title('WER for command: ' + str(i+1))
    plt.yticks([x for x in range(0, 110, 10)])
    plt.savefig('CommandWer/wer_command_'+str(i+1)+'.png')

