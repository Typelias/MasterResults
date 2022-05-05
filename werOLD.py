import matplotlib.pyplot as plt
import numpy as np
from utils import getCommandWERForModels, getAvg, getMax, getMin

models = ['silero', 'brain', 's2t', 'ws']


x = np.array([x for x in range(len(models)+1)][1:])
print(len(x))

for i in range(10):
    model_mean = getCommandWERForModels(models, getAvg, i)
    model_max = getCommandWERForModels(models, getMax, i)
    model_min = getCommandWERForModels(models, getMin, i)
    plt.figure(figsize=(10, 10))
    plt.bar(x, model_max, color='r', label='Max')
    plt.bar(x, model_mean, color='g', label='Mean')
    plt.bar(x, model_min, color='b', label='Min')

    plt.legend()
    plt.title('WER for command: ' + str(i+1))
    plt.ylabel('WER (%)')
    plt.xlabel('Model')
    plt.yticks([x for x in range(0, 110, 10)])
    plt.xticks(x, ['Silero STT', 'SpeechBrain wav2vec2', 'Facebook Speech2Text', 'WebSpeech API'],)
    plt.savefig('CommandWer/wer_command_'+str(i+1)+'.png')
    plt.clf()
