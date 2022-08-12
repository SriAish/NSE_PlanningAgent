import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(6, 3))
plt.rcParams.update({'font.size': 12})

x =  ['4X1 - NSE Encountered', '4X2 - NSE Encountered']

labels = ['Initial', 'LMDP Learned', 'LMDP Optimal', 'CMDP']

y = [[1, 0.9529],
        [1, 0.98],
        [1, 0.95],
        [0, 0.0969]]
# print(y)

type = ['#a52a2a', 'm', 'y', 'b']

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
        plt.bar(br[i], y[i], color =type[i], width = barWidth,
                edgecolor ='grey', label =labels[i])

barWidth = 0.3
plt.xticks([r + barWidth for r in range(len(y[0]))], x)

# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Mean NSE encountered')
# plt.xlabel('Toy Problem Configuration')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=4)
# legend = plt.legend(loc='upper right', shadow=True, fontsize='x-small')
# function to show the plot
# plt.show()
plt.savefig('plots/toy_problem.png',bbox_inches='tight')

