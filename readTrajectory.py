import pickle

def read_file(name):
    file_to_read = open(name, "rb")
    policy = pickle.load(file_to_read)