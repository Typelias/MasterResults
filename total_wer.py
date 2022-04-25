import matplotlib.pyplot as plt
import numpy as np
from utils import getAvgForModels


models = ['silero', 'brain', 's2t', 'ws']
x = np.array([x for x in range(len(models)+1)][1:])
avg_wer = getAvgForModels(models, 'avgWer')
avg_dirty = getAvgForModels(models, 'avgDirty')
avg_clean = getAvgForModels(models, 'avgClean')

plt.figure(figsize=(5, 7))
plt.bar(x - 0.3, avg_wer, width=0.3, label='Total Mean', color='#ff0000')
plt.bar(x, avg_dirty, width=0.3, label='Dirty Mean', color='#00ff00')
plt.bar(x + 0.3, avg_clean, width=0.3, label='Clean Mean', color='#0000ff')
plt.legend()
plt.xticks(x, models)
plt.xlabel('Model')
plt.ylabel('WER (%)')

plt.savefig('total_wer.png')
