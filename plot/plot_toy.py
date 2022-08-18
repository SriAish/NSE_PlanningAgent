import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(3, 3))
plt.rcParams.update({'font.size': 12})

x =  ['4X1', '4X2']

labels = ['Initial', 'LMDP Learned', 'LMDP Optimal', 'CASP']

y = [[1, 0.9506],
        [1, 0.9537],
        [1, 0.9522],
        [0, 0]]

y_error = [[0, 0.2167],
                [0, 0.210],
                [0, 0.2148],
                [0, 0]]

# for i in range(len(y_error)):
#         for j in range(len(y_error[i])):
#                 y_error[i][j] = y_error[i][j]/100
# print(y)

type = ['#d30b0b', '#009900', '#a64da6', '#05aeef']

# print(y)
# plotting the points 
# set width of bar
barWidth = 0.2

br = []

br.append(np.arange(len(y[0])))
for i in range(1, len(y)):
        br.append([x + barWidth for x in br[i-1]])

print(br)

for i in range(len(y)):
        plt.bar(br[i], y[i], yerr=y_error[i], align='center', alpha=0.5, ecolor='black', capsize=3, color =type[i], width = barWidth,
                edgecolor ='grey', label =labels[i])

barWidth = 0.3
plt.xticks([r + barWidth for r in range(len(y[0]))], x)

# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Average NSE encountered')
# plt.xlabel('Toy Problem Configuration')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# legend = plt.legend(loc='upper right', shadow=True, fontsize='x-small')
# function to show the plot
# plt.show()
plt.savefig('plots/toy_problem.png',bbox_inches='tight')

