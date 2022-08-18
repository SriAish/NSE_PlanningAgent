import random
import pickle

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

# severe = load("severe_trajectories_15_15_35")
mild = load("policy/FSA_LP_p1_15_15_0_1_0.pkl")
# no_nse = load("no_nse_trajectories_15_15_35")
s = []
m = []
n = []

for s in mild:
    print(s)
    print(mild[s])

# for r in mild:
#     if len(r) < 25:
#         m += [r]


# print(len(m))


# save("s_7_7_35", m)
# save("BP_test_15_15_35_set", R_test)