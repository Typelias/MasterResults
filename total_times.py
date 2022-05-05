import matplotlib.pyplot as plt
import numpy as np

from utils import getAvgForModels

models_fetch = ['silero', 'silero_server', 'brain', 's2t']
models = ['Silero STT Oculus', 'Silero STT Server', 'Brain', 'S2T']

avgTime = getAvgForModels(models_fetch, 'avgTime') / 1000

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

ax1.bar(models, avgTime, color=['#3274A1', '#E1812C', '#40943c', '#bf3d3d'])
ax2.bar(models, avgTime, color=['#3274A1', '#E1812C', '#40943c', '#bf3d3d'])

ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

ax1.set_ylim(2, 4)
ax2.set_ylim(0, 0.2)

d = .5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
            linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

fig.supylabel("Time(s)")
fig.supxlabel("Model")
fig.suptitle("Mean time for all commands")

plt.savefig('Time/time_all_commands.png')

plt.clf()

totalTime = (getAvgForModels(models_fetch, 'totalTime') / 1000) / 60

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

ax1.bar(models, totalTime, color=['#3274A1', '#E1812C', '#40943c', '#bf3d3d'])
ax2.bar(models, totalTime, color=['#3274A1', '#E1812C', '#40943c', '#bf3d3d'])

ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

ax1.set_ylim(30, 75)
ax2.set_ylim(0, 3)

d = .5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
            linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

fig.supylabel("Time(min)")
fig.supxlabel("Model")
fig.suptitle("Total time for benchmarks")

plt.savefig('Time/time_benchmark.png')

