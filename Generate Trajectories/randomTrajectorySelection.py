import pickle
import random

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)


mild = load("mild_trajectories")

print(random.sample(list(mild), 1))