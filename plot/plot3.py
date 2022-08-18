import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(4, 4))
plt.rcParams.update({'font.size': 12})
labels =  ['Config 1 Severe', 'Config 1 Mild', 'Config 2 Severe', 'Config 2 Mild', 'Config 3 Severe', 'Config 3 Mild']

x = ['4 nodes', '6 nodes', '8 nodes']

# y = [[0.1, 0.1, 0.1, 0.2, 0.2, 0.3],
#         [0.1009, 0.1686, 0.0987, 0.1633, 0.3984, 0.1251],
#         [0.1029, 0.1621, 0.2768, 0.1180, 0.5786, 0.0783],
#         [0.1125, 0.1507, 0.1339, 0.2612, 0.2794, 0.2698],
#         [0.1062, 0.1062, 0.1355, 0.2584, 0.2939, 0.2526]]
lab_scatter = ['Config 1 Severe limit', 'Config 1 Mild limit', 'Config 2 Severe limit', 'Config 2 Mild limit', 'Config 3 Severe limit', 'Config 3 Mild limit']
y_line = [[0.1, 0.1, 0.1], [0.1, 0.1, 0.1], [0.1, 0.1, 0.1], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.3, 0.3, 0.3]]
y_val = [0.1, 0.2, 0.3]
col = ['yellow', '#ffffe0', 'blue', '#add8e6', 'black', 'grey']
col = ['k', 'm', 'r', 'b', '#3a0d63', 'g', 'y']
y = [[0.1009, 0.1686, 0.0987, 0.1633, 0.3984, 0.1251],
        [0.1029, 0.1621, 0.2768, 0.1180, 0.5786, 0.0783],
        [0.1125, 0.1507, 0.1339, 0.2612, 0.2794, 0.2698]]
y = [[y[j][i] for j in range(len(y))] for i in range(len(y[0]))]
y_error = [[0.30, 0.37, 0.45, 0.32, 0.5, 0.33],
                [0.32, 0.36,  0.45, 0.32, 0.49, 0.27],
                [0.31, 0.37, 0.34, 0.44, 0.45, 0.44]]
y_error = [[y_error[j][i] for j in range(len(y_error))] for i in range(len(y_error[0]))]

for i in range(len(y_error)):
        for j in range(len(y_error[i])):
                y_error[i][j] = y_error[i][j]/100
# print(y)
m = ['^', 'o', '^', 'o', '^', 'o']
type = ['#e41c1c', '#009900', '#33ff33', '#a64da6', '#dbb7db', '#05aeef', '#9999ff']
br = []
barWidth = 0.1
br.append(np.arange(len(y[0])))
for i in range(1, len(y)):
        br.append([x + barWidth for x in br[i-1]])
# print(y)
# plotting the points 
for i in range(len(y)):
        # print(y[i], y_error[i])
        plt.bar(br[i], y[i], yerr=y_error[i], align='center', alpha=0.5, ecolor='black', capsize=3, color =type[i], width = barWidth,
                edgecolor ='grey', label=labels[i], zorder=-1)
for i in range(len(y)):
        plt.scatter(br[i], y_line[i], c=col[i], marker=m[i], s=35, zorder=1, label=lab_scatter[i])

for i in y_val:
        y_ma = np.full(len(x)+1,i)
        x_ma = []
        # k = 0
        for j in range(len(x)):
                x_ma.append(j-0.25)
        x_ma.append(len(x)-0.25)
        plt.plot(x_ma, y_ma, '-k', zorder=0)

barWidth = 0.25
plt.xticks([r + barWidth for r in range(len(y[0]))], x)
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# legend = ax.legend(loc='upper center', shadow=True, fontsize='x-small')
# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Average NSE encountered')
  
# function to show the plot
# plt.show()
plt.savefig('plots/FSAsizevsThrehold_2.png',bbox_inches='tight')


