import pickle
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})
states = [4, 5, 6, 7, 8, 9, 10, 11]
# print(y)
time = [[0.2962, 14.9342, 0.2398, 7.5627, 10.5042, 4.9675, 3.1875, 7.2229, 6.9269, 11.3613], [40.6810, 51.9597, 66.2073, 3.3110, 45.8716, 3.3106, 67.8158, 10.7605, 71.7549, 183.7033],
        [318.1072, 138.5736, 8.0303, 64.9962, 65.1126, 5.9483, 11.5353, 128.8136, 7.9299, 16.4319], [8.8114, 310.8167, 1226.8434, 974.3876, 304.5833, 23.8720, 312.2107, 214.1299, 484.6599, 5.2961],
        [21.8981, 596.4119, 10.0652, 8.4106, 407.1425, 625.9418, 28.6873, 1131.4355, 25.3281, 392.8738], [51.2148, 1027.9044, 1713.1916, 42.1935, 93.5457, 1933.6656, 45.1355, 27.0170, 30.0440, 1348.4279],
        [3021.3838, 324.0757, 766.9358, 1801.3067, 62.3013, 5687.4348, 30.9696, 6128.7509, 4666.2685, 6180.6009], [4830.3405, 7731.7694, 23.3540, 7705.2509, 2372.6088, 18402.2032, 2232.4956, 4895.7557, 4409.0711, 87.1423]]
# time = [545.37, 765.48, 3865.61, 3248.19, 6312.34, 28670.02, 52689.99]
# time = [t/60 for t in time]
for ti in range(len(time)):
        for t in range(len(time[ti])):
                time[ti][t] = time[ti][t]/60
t_mean = []
t_std = []

for ti in time:
        t_mean += [np.mean(ti)]
        t_std += [np.std(ti)]

best_acc = [0.670, 0.680, 0.690, 0.860, 0.914, 0.913, 0.860, 0.945]
best_acc = [b*100 for b in best_acc]

# print(y)
# plt.plot(states, best_acc, '-b')
# plotting the points 
# plt.scatter(states, t_mean, c='blue')
# print(t_std)
plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std), color='lightblue')
plt.scatter(states, t_mean, c='blue', s = 15)
# # naming the x axis
plt.xlabel('Number of states')
# naming the y axis
plt.ylabel('Time (in Minutes)')
  
# function to show the plot
plt.show()


