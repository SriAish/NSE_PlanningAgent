import pickle
import matplotlib.pyplot as plt

states = [5, 6, 7, 8, 9, 10, 11]
# print(y)
time = [545.37, 765.48, 3865.61, 3248.19, 6312.34, 28670.02, 52689.99]
time = [t/60 for t in time]

best_acc = [0.521, 0.551, 0.784, 0.872, 0.878, 0.868, 0.922]
best_acc = [b*100 for b in best_acc]

# print(y)
# plotting the points 
plt.plot(states, best_acc)
  
# naming the x axis
plt.xlabel('Number of states')
# naming the y axis
plt.ylabel('Accuracy in %')
  
# function to show the plot
plt.show()


