import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])

totalTimes = [2802.090, 152.060, 156.080, 145.343, 386.165]
avgTimes = [2335.108, 126.716, 130.066, 121.119, 1988.471]


plt.figure(figsize=(10, 7))

plt.subplot(1, 2, 1)
plt.bar(x, totalTimes, label='Total Time', color='#ff0000')
plt.xticks(x, ['silero oculus', 'silero server', 'sb', 's2t', 'kaldi' ], rotation=15, ha="right")
plt.xlabel('Model')
plt.ylabel('Time (s)')
plt.title('Time to compleete Benchmark')

plt.subplot(1, 2, 2)
plt.bar(x, avgTimes, label='Average Time', color='#00ff00')
plt.xticks(x, ['silero oculus', 'silero server', 'sb', 's2t', 'kaldi' ], rotation=15, ha="right")
plt.xlabel('Model')
plt.ylabel('Time (ms)')
plt.title('Average Time per Command')

plt.savefig('total_times.png')
