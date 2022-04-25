import matplotlib.pyplot as plt
import numpy as np
from utils import getCommandTimeForModels, getAvg, getStd

models = ['silero', 'silero_server', 'brain', 's2t']
model_names = ['silero Oculus', 'silero Server', 'Brain', 'S2T']


x = np.array([x for x in range(len(models)+1)][1:])
print(len(x))

for i in range(10):
    model_mean = getCommandTimeForModels(models, getAvg, i)
    model_std = getCommandTimeForModels(models, getStd, i)
    plt.title('Mean Time for command: ' + str(i+1))
    plt.ylabel('Time (ms)')
    plt.xlabel('Model')
    plt.xticks(x, model_names)
    plt.yticks([x for x in range(0, 6500, 500)])
    plt.bar(x, model_mean, width=0.3, color='g', label='Mean', yerr=model_std)
    plt.savefig('CommandTime/time_command_'+str(i+1)+'.png')
