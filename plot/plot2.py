from cProfile import label
import pickle
import matplotlib.pyplot as plt
import numpy as np
import sys

plt.figure(figsize=(3, 3))
plt.rcParams.update({'font.size': 12})
labels = ['Initial', 'LMDP learnt - 20% slack', 'LMDP learnt - 25% slack', 'LMDP optimal - 20% slack', 'LMDP optimal - 25% slack', 'CASP - 20% slack', 'CASP - 25% slack']

x = ['severe', 'mild']

y = [[0.9451, 0.0254],
        [0.9452, 0.0266],
        [0.9419, 0.0288],
        [0.9479, 0.0255],
        [0.9445, 0.0252],
        [0, 0],
        [0, 0]]
# print(y)

type = ['#d30b0b', '#009900', '#33ff33', '#a64da6', '#dbb7db', '#05aeef', '#9999ff']
mark = ['o', 'o', '^', 'o', '^', 'o', '^']
# print(y)
# plotting the points 
# fig, ax = plt.subplots()
for i in range(len(labels)):
        # print(type[i])
        plt.scatter(x, y[i], c=type[i], marker=mark[i], label=labels[i], s=15)

legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# plt.xlabel("NSE", labelpad=2)
# naming the y axis
plt.ylabel('Average NSE encountered')
# xtick_loc = [0.20, 0.40]
# ax.set_xticks(xtick_loc)
# function to show the plot
plt.savefig('plots/ApptoachvsNSE.png',bbox_inches='tight')
# plt.show()


