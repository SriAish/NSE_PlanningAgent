from cProfile import label
import pickle
import matplotlib.pyplot as plt
import numpy as np
import sys

plt.figure(figsize=(9, 3))
plt.rcParams.update({'font.size': 12})
labels = ['Initial', 'LMDP learnt - 20% slack', 'LMDP learnt - 25% slack', 'LMDP optimal - 20% slack', 'LMDP optimal - 25% slack', 'CMDP - 20% slack', 'CMDP - 25% slack']

x = ['severe', 'mild']

y = [[1, 0],
        [0.9452, 0.0266],
        [0.9419, 0.0288],
        [0.9479, 0.0255],
        [0.9445, 0.0252],
        [0, 0],
        [0, 0]]
# print(y)

type = ['-k', '-r', '--r', '-y', '--y', '-b', '--b']

# print(y)
# plotting the points 
fig, ax = plt.subplots()
for i in range(len(labels)):
        ax.plot(x, y[i], type[i], label=labels[i])

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-small')
# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Mean NSE encountered')
  
# function to show the plot
plt.savefig('plots/ApptoachvsNSE.png',bbox_inches='tight')
# plt.show()


