import matplotlib.pyplot as plt
import numpy as np

from utils import getAvgForModels

models = ['silero', 'silero_server', 'brain', 's2t']

x = np.array([x for x in range(len(models)+1)][1:])

avgTime = getAvgForModels(models, 'avgTime')
totalTime = getAvgForModels(models, 'totalTime')

plt.figure(figsize=(5, 10))
plt.bar(x, avgTime, color='g', label='Mean')
plt.xticks(x, models)
plt.ylabel('Time (ms)')
plt.xlabel('Model')
plt.yticks([x for x in range(0, 3600, 100)])
plt.title('Mean Time for all commands')
plt.savefig('Time/time_all_commands.png')

plt.clf()

plt.bar(x, totalTime/1000, color='g', label='Mean')
plt.xticks(x, models)
plt.ylabel('Time (s)')
plt.xlabel('Model')
plt.yticks([x for x in range(0, 4300, 100)])

plt.title('Total Time for benchmark')
plt.savefig('Time/time_benchmark.png')
