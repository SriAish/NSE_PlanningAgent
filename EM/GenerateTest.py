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
    if b >= 7:
        traj += [1]
    else:
        traj += [0]

    return traj

def generate_trajectories(n):
    r0 = []
    r1 = []
    lr = 0
    while n:
        r = get_traj()
        if r[-1] == 0:
            r0 += [tuple(r)]
            # r0.add(tuple(r))
        else:
            r1 += [tuple(r)]
            # r1.add(tuple(r))
        if lr < len(r0) + len(r1):
            lr = len(r0) + len(r1)
            n -= 1
    print(len(r0), len(r1))

    if len(r1) > len(r0):
        r1_ = random.sample(list(r1), len(r0))
        r0_ = r0
    else:
        r0_ = random.sample(list(r0), len(r1))
        r1_ = r1
    R = list(r0_) + list(r1_)
    print(len(r1_), len(r0_))
    # R = list(r0)+list(r1)
    return R

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

R = generate_trajectories(100000)
print(random.sample(list(R), 10), len(R))
random.shuffle(R)
n = round(0.8*len(R))
R_train = R[:n]
R_test = R[n:]

c0 =0
c1 = 0
for r in R_test:
    if r[-1] == 0:
        c0+=1
    else:
        c1+=1


save("R7_train", R_train)
save("R7_test", R_test)

print(c0, c1)