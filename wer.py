import matplotlib.pyplot as plt
import numpy as np
from utils import getCommandWERForModels, getAvg, getMax, getMin


# arr = fetchResultMap('brain', True)

# print(getAvg(arr)*100)

models = ['silero', 'brain', 's2t', 'ws']


x = np.array([x for x in range(len(models)+1)][1:])
print(len(x))

for i in range(10):
    model_mean = getCommandWERForModels(models, getAvg, i)
    model_max = getCommandWERForModels(models, getMax, i)
    model_min = getCommandWERForModels(models, getMin, i)

    plt.bar(x, model_max, width=0.3, color='r', label='Max')
    plt.bar(x, model_mean, width=0.3, color='g', label='Mean')
    plt.bar(x, model_min, width=0.3, color='b', label='Min')

    plt.legend()
    plt.title('WER for command: ' + str(i+1))
    plt.ylabel('WER (%)')
    plt.xlabel('Model')
    plt.xticks(x, models)
    plt.savefig('CommandWer/wer_command_'+str(i+1)+'.png')
    plt.clf()
