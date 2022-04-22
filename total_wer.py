import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4, 5, 6])

avg_wer = [26.149,26.149, 13.962, 33.293, 100, 1.671]
avg_dirty = [30.024, 30.024, 16.171, 42.416, 100, 1.933]
avg_clean = [22.274, 22.274, 11.754, 25.170, 100, 1.409]

plt.figure(figsize=(5,7))
plt.bar(x - 0.3, avg_wer, width=0.3, label='Total Mean', color='#ff0000')
plt.bar(x, avg_dirty, width=0.3, label='Dirty Mean', color='#00ff00')
plt.bar(x + 0.3, avg_clean, width=0.3, label='Clean Mean', color='#0000ff')
plt.legend()
plt.xticks(x, ['silero oculus', 'silero server', 'sb', 's2t', 'Kaldi', 'WebSpeech'], rotation=15, ha="right")
plt.xlabel('Model')
plt.ylabel('WER (%)')

plt.savefig('total_wer.png')