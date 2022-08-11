import pickle
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})

x =  ['4X1 - NSE Encountered', '4X2 - NSE Encountered']

labels = ['LMDP Learned', 'LMDP Optimal', 'CMDP']

y = [[1, 0.98],
        [1, 0.95],
        [0, 0.0969]]
# print(y)

type = ['m', 'y', 'b']

# print(y)
# plotting the points 
# set width of bar
barWidth = 0.25

br = []

br.append(np.arange(len(y[0])))
for i in range(1, len(y)):
        br.append([x + barWidth for x in br[i-1]])

print(br)

for i in range(len(y)):
        plt.bar(br[i], y[i], color =type[i], width = barWidth,
                edgecolor ='grey', label =labels[i])

plt.xticks([r + barWidth for r in range(len(y[0]))], x)

# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Mean NSE encountered')
plt.xlabel('Toy Problem Configuration')
legend = plt.legend(loc='upper right', shadow=True, fontsize='x-small')
# function to show the plot
plt.show()


