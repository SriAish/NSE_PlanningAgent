import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(3, 3))
plt.rcParams.update({'font.size': 12})

x =  ['4X1', '4X2']

labels = ['Initial - Average', 'Initial - Std', 'LMDP Learned - Average', 'LMDP Learned Std', 'LMDP Optimal - Average', 'LMDP Optimal - Std', 'CMDP - Average', 'CMDP - Std']

y = [[1, 0.9506],
        [0, 0.2167],
        [1, 0.9537],
        [0, 0.210],
        [1, 0.9522],
        [0, 0.2148],
        [0, 0],
        [0, 0]]
# print(y)

type = ['#a52a2a', '#cc6600', '#ff3333', '#f07474', '#cccc00', '#ffb266', '#3399ff', '#9999ff']

# print(y)
# plotting the points 
# set width of bar
barWidth = 0.1

br = []

br.append(np.arange(len(y[0])))
for i in range(1, len(y)):
        br.append([x + barWidth for x in br[i-1]])

print(br)

for i in range(len(y)):
        plt.bar(br[i], y[i], color =type[i], width = barWidth,
                edgecolor ='grey', label =labels[i])

barWidth = 0.35
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

