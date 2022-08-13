from cProfile import label
import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(4, 4))
plt.rcParams.update({'font.size': 12})
labels =  ['Config 1 Severe', 'Config 1 Mild', 'Config 2 Severe', 'Config 2 Mild', 'Config 3 Severe', 'Config 3 Mild']

y_line = [0.1, 0.2, 0.3]

x = ['5 nodes', '7 nodes', '9 nodes']

y = [[1, 0, 1, 0, 0.2649, 0],
        [0.1329, 0.0, 0.1372, 0, 0.2675, 0],
        [0.3959, 0.0, 0.3908, 0.0, 0.3902, 0.0]]
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

for i in y_line:
        y_ma = np.full(len(x)+1,i)
        x_ma = []
        # k = 0
        for j in range(len(x)):
                x_ma.append(j-0.25)
        x_ma.append(len(x)-0.25)
        plt.plot(x_ma, y_ma, '-k')

barWidth = 0.25
plt.xticks([r + barWidth for r in range(len(y[0]))], x)

legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# legend = ax.legend(loc='upper center', shadow=True, fontsize='x-small')
# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Mean NSE encountered')
  
# function to show the plot
# plt.show()
plt.savefig('plots/FSAsizevsThrehold_Nav.png',bbox_inches='tight')


