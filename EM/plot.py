import pickle
import matplotlib.pyplot as plt

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
y = load("results/objective/new_BP_15_15_35_15_8_8")
# print(y)
x = [*range(len(y))]

# print(y)
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('iteration')
# naming the y axis
plt.ylabel('objective value')
  
# function to show the plot
plt.show()


