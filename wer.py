import matplotlib.pyplot as plt
import numpy as np
from utils import getCommandWERForModels, getAvg, getMax, getMin


# arr = fetchResultMap('brain', True)

# print(getAvg(arr)*100)

models = ['silero', 'brain', 's2t']


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
        plt.title('WER for command: '+ str(i+1))
        plt.ylabel('WER (%)')
        plt.xlabel('Model')
        plt.xticks(x, models)
        plt.savefig('CommandWer/wer_command_'+str(i+1)+'.png')
        plt.clf()








# sb_wer = getAvg(fetchResultMap('brain', True))*100
# sb_min = getMin(fetchResultMap('brain', True))*100
# sb_max = getMax(fetchResultMap('brain', True))*100
# sb_yerr = [np.subtract(sb_wer, sb_min), np.subtract(sb_max, sb_wer)]

# s2t_wer = getAvg(fetchResultMap('s2t', True))*100
# s2t_min = getMin(fetchResultMap('s2t', True))*100
# s2t_max = getMax(fetchResultMap('s2t', True))*100
# s2t_yerr = [np.subtract(s2t_wer, s2t_min), np.subtract(s2t_max, s2t_wer)]


# # ws = [0, 2.083, 0, 0, 0, 0, 0.833, 6.845, 6.944, 0]
# # ws_std = [0, 6.910, 0, 0, 0, 0, 2.764, 13.240, 14.367, 0]


# width = 0.2

# plt.figure(figsize=(10, 5))
# plt.bar(x - (width*2), silero_wer, width=width,
#         label='Silero Oculus', color='#ff0000', yerr=silero_yerr, capsize=3)
# plt.bar(x-width, silero_wer, width=width, label='Silero Server',
#         color='#FF00FF', yerr=silero_yerr, capsize=3)
# plt.bar(x, sb_wer, width=width, label='SB',
#         color='#00ff00', yerr=sb_yerr, capsize=3)
# plt.bar(x + width, s2t_wer, width=width, label='S2T',
#         color='#0000ff', yerr=s2t_yerr, capsize=3)

# # plt.bar(x+(width*3), ws, width=width, label='WebSpeech', color='#00FFFF')

# plt.yticks(np.arange(0, 105, 5))
# plt.xticks(np.arange(0, 11, 1))
# plt.xlabel('Command')
# plt.ylabel('WER (%)')
# plt.legend()
# # plt.ylim(0)
# plt.savefig('wer.png')
