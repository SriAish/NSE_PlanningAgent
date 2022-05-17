import pickle

def load(name):
    file_to_read = open(name, "rb")
    return pickle.load(file_to_read)

x = load('severe_trajectories_7')

print(x)