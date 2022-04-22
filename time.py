import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

silero_time = [1948.378, 2464.686, 2261.842, 1947.677,
              2088.750, 1771.138, 3217.579, 3877.360, 2647.878, 2125.608]
silero_time_std = [379.150, 457.594, 343.415, 331.277, 300.931, 207.425, 509.194, 426.836, 389.567, 440.130]
sb_time = [127.277, 137.723, 123.312, 110.010, 139.534, 117.670, 149.025, 136.857, 133.034, 126.223]
sb_time_std = [29.762, 30.322, 21.106, 15.771, 57.484, 27.437, 21.082, 35.526, 21.154, 32.685]

s2t_time = [107.289, 128.473, 123.833, 101.662, 119.342, 98.779, 159.861, 132.139, 136.842, 102.982]
s2t_time_std = [74.579, 45.510, 50.693, 15.099, 14.750, 20.861, 97.829, 17.795, 18.310, 16.976]

silero_server_time = [119.580, 134.708, 152.060, 115.607, 114.987, 105.111, 154.830, 129.966, 162.687, 98.540]
silero_server_time_std = [96.582, 119.380, 114.031, 83.141, 76.190, 55.586, 108.894, 83.250, 122.492, 53.911]

kaldi_time = [1800.052, 2341.468, 2124.486, 1393.822, 589.659, 838.543, 3220.830, 2895.459, 2658.430, 2021.957]
kaldi_time_std = [404.448, 470.210, 310.297, 636.573, 78.136, 542.252, 452.721, 450.233, 399.810, 420.415]

width = 0.15

plt.bar(x - (2*width), silero_time, width=width, label='Silero Oculus',
        color='#ff0000', yerr=silero_time_std)
plt.bar(x-width, silero_server_time, width=0.2, label='Silero Server', color='#FF00FF',yerr=silero_server_time_std)
plt.bar(x, sb_time, width=width, label='SB', color='#00ff00', yerr=sb_time_std)
plt.bar(x + width, s2t_time, width=0.2, label='S2T', color='#0000ff', yerr=s2t_time_std)
plt.bar(x+(width*2), kaldi_time, width=width, label='Kaldi', color='#FFFF00', yerr=kaldi_time_std)

# plt.bar(x+0.2, s2t, width=0.2, label='S2T', color='#0000ff')
# plt.bar(x+0.4, silero_server, width=0.2,
#         label='Silero Server', color='#ff00ff')
m = max(silero_time) + 200
plt.yticks(np.arange(0, m, 200))
plt.xticks(np.arange(0,11,1))
plt.xlabel('Command')
plt.ylabel('Time (ms)')
plt.legend()
plt.savefig('times.png')
