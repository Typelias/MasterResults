import matplotlib.pyplot as plt
import numpy as np
from utils import getAvgForModels


models = ['silero', 'brain', 's2t', 'ws']
x = np.array([x for x in range(len(models)+1)][1:])
avg_wer = getAvgForModels(models, 'avgWer') * 100
avg_dirty = getAvgForModels(models, 'avgDirty') * 100
avg_clean = getAvgForModels(models, 'avgClean') * 100

plt.figure(figsize=(10, 10))
plt.bar(x - 0.3, avg_dirty, width=0.3, label='Noisy Mean')
plt.bar(x, avg_wer, width=0.3, label='Total Mean')
plt.bar(x + 0.3, avg_clean, width=0.3, label='Clean Mean')
plt.legend()
plt.xticks(x, ['Silero STT', 'SpeechBrain wav2vec2', 'Facebook Speech2Text', 'WebSpeech API'],)
plt.xlabel('Model')
plt.ylabel('WER (%)')

plt.savefig('total_wer.png')
