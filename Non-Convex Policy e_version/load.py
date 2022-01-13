import pickle

def load(name):
    file_to_read = open(name, "rb")
    return pickle.load(file_to_read)

x = load('severe_trajectories_3')

print(x)