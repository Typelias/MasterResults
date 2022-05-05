import matplotlib.pyplot as plt
import numpy as np
from utils import getCommandTimeForModels, getAvg, getStd

models = ['silero', 'silero_server', 'brain', 's2t']
model_names = ['Silero STT Oculus', 'Silero STT Server', 'Brain', 'S2T']

for i in range(10):
    model_mean = getCommandTimeForModels(models, getAvg, i)/1000
    model_std = getCommandTimeForModels(models, getStd, i)/1000

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True, )
    fig.subplots_adjust(hspace=0.05)

    ax1.bar(model_names, model_mean, color=['#3274A1', '#E1812C', '#40943c', '#bf3d3d'], label='Mean', yerr=model_std, capsize=10, edgecolor='k')
    ax2.bar(model_names, model_mean, color=['#3274A1', '#E1812C', '#40943c', '#bf3d3d'], label='Mean', yerr=model_std, capsize=10, edgecolor='k')

    ax1.set_ylim(model_mean[0] - model_std[0] - 1, model_mean[0] + model_std[0] + 1)
    ax2.set_ylim(0, np.array(model_mean[1:]).max() + 0.2)

    ax1.spines.bottom.set_visible(False)
    ax2.spines.top.set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)
    ax2.xaxis.tick_bottom()

    d = .5
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
                linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

    fig.supylabel("Time(s)")
    fig.supxlabel("Model")
    fig.suptitle("Mean Time for command: " + str(i+1))

    plt.savefig('CommandTime/time_command_'+str(i+1)+'.png')


