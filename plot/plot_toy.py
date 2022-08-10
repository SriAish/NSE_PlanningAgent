import pickle
import matplotlib.pyplot as plt
import numpy as np

x =  ['4X1 - NSE Encountered', '4X2 - NSE Encountered']

labels = ['LMDP Optimal', 'CMDP']

y = [[1, 0.95],
        [0, 0.0969]]
# print(y)

type = ['-y', '-b']

# print(y)
# plotting the points 
fig, ax = plt.subplots()
for i in range(len(labels)):
        ax.plot(x, y[i], type[i], label=labels[i])

legend = ax.legend(loc='center right', shadow=True, fontsize='x-small')
# print(t_std)
# plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std))
# naming the x axis
# plt.xlabel('NSE')
# naming the y axis
plt.ylabel('Mean NSE encountered')
plt.xlabel('Toy Problem Configuration')
# function to show the plot
plt.show()


