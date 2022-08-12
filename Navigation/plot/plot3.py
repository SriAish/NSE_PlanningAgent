from cProfile import label
import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 12})
labels =  ['Configuration 1 Severe', 'Configuration 1 Mild', 'Configuration 2 Severe', 'Configuration 2 Mild', 'Configuration 3 Severe', 'Configuration 3 Mild']

x = ['Set NSE Threshold', 'CMDP (4 nodes)', 'CMDP (6 nodes)', 'CMDP (8 nodes)']

y = [[0.1, 0.1, 0.1, 0.2, 0.2, 0.3],
        [0.1009, 0.1686, 0.0987, 0.1633, 0.3984, 0.1251],
        [0.1029, 0.1621, 0.2768, 0.1180, 0.5786, 0.0783],
        [0.1125, 0.1507, 0.1339, 0.2612, 0.2794, 0.2698],
        [0.1062, 0.1062, 0.1355, 0.2584, 0.2939, 0.2526]]
y = result = [[y[j][i] for j in range(len(y))] for i in range(len(y[0]))]
# print(y)

type = ['k', 'm', 'r', 'b', 'c', 'g', 'y']
br = []
barWidth = 0.1
br.append(np.arange(len(y[0])))
for i in range(1, len(y)):
        br.append([x + barWidth for x in br[i-1]])
# print(y)
# plotting the points 
for i in range(len(y)):
        plt.bar(br[i], y[i], color =type[i], width = barWidth,
                edgecolor ='grey', label=labels[i])

barWidth = 0.25
plt.xticks([r + barWidth for r in range(len(y[0]))], x)

legend = plt.legend(loc='upper right', shadow=True, fontsize='x-small')
# legend = ax.legend(loc='upper center', shadow=True, fontsize='x-small')
# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Mean NSE encountered')
  
# function to show the plot
plt.show()


