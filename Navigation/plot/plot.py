import pickle
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(4, 3))
plt.rcParams.update({'font.size': 12})
states = ['4', '5', '6', '7', '8', '9']
# print(y)
time = [[3.219, 3.194, 557.477, 58.302, 35.959, 44.22, 12.766, 947.074, 45.724, 12.75], 
        [236.26, 178.844, 4.576, 129.13, 113.075, 1610.309, 1595.264, 767.758, 767.157, 2167.811],
        [1348.291, 1722.905, 1345.952, 4626.718, 1537.033, 904.661, 1530.826, 586.6346, 1451.780, 7473.199], 
        [2691.855, 3337.692, 3171.520, 1770.680, 1935.651, 2811.112, 5006.279, 2311.955, 5270.925, 2092.842],
        [5277.514, 5753.857, 31989.891, 5743.747, 9358.218, 5127.068, 9432.449, 5435.869, 11376.190, 46301.745],
        [16560.623, 14976.481, 14976.481, 10637.283, 15097.183, 4438.435, 6797.7885, 13187.742, 18605.561]]
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

# best_acc = [0.673, 0.668, 0.668, 0.8819, 0.909]
# best_acc = [b*100 for b in best_acc]

# print(y)
# plt.plot(states, best_acc, '-b')
# plotting the points 
plt.scatter(states, t_mean, c='blue')
print(t_std)
plt.fill_between(states, np.array(t_mean)-np.array(t_std), np.array(t_mean)+np.array(t_std), color='lightblue')
plt.scatter(states, t_mean, c='blue', s = 12)
# # naming the x axis
plt.xlabel('Number of states')
# naming the y axis
plt.ylabel('Time (in Minutes)')
plt.savefig('plots/nodesvstime_nav.png',bbox_inches='tight')
# function to show the plot
# plt.show()


