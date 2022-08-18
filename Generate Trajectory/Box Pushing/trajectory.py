import random
import pickle

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

# severe = load("severe_trajectories_15_15_35")
nn = load("new_nn")
mild = load("BP_test_15_15_35_set")
# no_nse = load("no_nse_trajectories_15_15_35")
s = []
m = []
n = []

s_c = 0
m_c = 0
n_c = 0
mild = mild + nn + nn + nn[:-11]
for r in mild:
    m += [r]
    if r[-1] == 'S':
        s_c += 1
    elif r[-1] == 'M':
        m_c += 1
    else:
        n_c += 1
        # print(r)

print(s_c, m_c, n_c)
print(len(m))


save("new_test", m)
# save("BP_test_15_15_35_set", R_test)