import pickle

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)