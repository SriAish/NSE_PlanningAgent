import random
import pickle

def get_sym(t = 0, b = False):
    v = random.random()

    if t==1:
        if v <= 0.5:
            return 'a'
        return 'b'

    # if b:
        # if v <= 0.5:
        #     return 'b'
        # return 'e'

    if v <= 0.4:
        return 'a'
    if v <= 0.8:
        return 'b'
    return 'e'

def get_traj():
    b = 0
    s = get_sym(1)
    traj = []

    while s != 'e':
        traj += s

        if s == 'b':
            b += 1
        s = get_sym()
    traj += s
    if b >= 2:
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

    if len(r1) > len(r0):
        r1_ = random.sample(list(r1), len(r0))
        r0_ = r0
    else:
        r0_ = random.sample(list(r0), len(r1))
        r1_ = r1
    R = r0_ + r1_
    print(r0_, len(r0_))
    # R = r0+r1
    return R

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

R = generate_trajectories(10000)
# print(R, len(R))
save("R3", R)