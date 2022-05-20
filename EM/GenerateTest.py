import random
import pickle

def get_sym(t = 0):
    v = random.random()

    if t==1:
        if v <= 0.5:
            return 'a'
        return 'b'

    if v <= 0.4:
        return 'a'
    if v <= 0.8:
        return 'b'
    return 'e'

def get_traj():
    b = False
    s = get_sym(1)
    traj = []

    while s != 'e':
        traj += s

        if s == 'b':
            b = True
        s = get_sym()
    traj += s
    if b:
        traj += [1]
    else:
        traj += [0]

    return traj

def generate_trajectories(n):
    r0 = []
    r1 = []
    while n:
        n -= 1
        r = get_traj()
        if r[-1] == 0:
            r0 += [r]
        else:
            r1 += [r]
    print(len(r0), len(r1))

    r1_ = random.sample(list(r1), len(r0))
    R = r0 + r1_
    return R

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

R = generate_trajectories(10000)
# print(R)
save("R1", R)