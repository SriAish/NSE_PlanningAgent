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
    if b > 0 and b <= 2:
        traj += [1]
    elif b > 2:
        traj += [2]
    else:
        traj += [0]

    return traj

def generate_trajectories(n):
    r0 = []
    r1 = []
    r2 = []
    lr = 0
    while n:
        r = get_traj()
        if r[-1] == 0:
            r0 += [tuple(r)]
            # r0.add(tuple(r))
        elif r[-1] == 1:
            r1 += [tuple(r)]
            # r1.add(tuple(r))
        else:
            r2 += [tuple(r)]
        if lr < len(r0) + len(r1) + len(r2):
            lr = len(r0) + len(r1) + len(r2)
            n -= 1
    print(len(r0), len(r1), len(r2))

    if len(r1) > len(r0) and len(r2) > len(r0):
        r0_ = r0
        r1_ = random.sample(list(r1), len(r0))
        r2_ = random.sample(list(r2), len(r0))
    elif len(r0) > len(r1) and len(r2) > len(r1):
        r0_ = random.sample(list(r0), len(r1))
        r1_ = r1
        r2_ = random.sample(list(r2), len(r1))
    else:
        r0_ = random.sample(list(r0), len(r2))
        r1_ = random.sample(list(r1), len(r2))
        r2_ = r2
    R = list(r0_) + list(r1_) + list(r2_)
    print(len(R))
    return R

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

R = generate_trajectories(1500)
print(random.sample(list(R), 10), len(R))
random.shuffle(R)
n = round(0.8*len(R))
R_train = R[:n]
R_test = R[n:]

c0 = 0
c1 = 0
c2 = 0
for r in R_test:
    if r[-1] == 0:
        c0+=1
    elif r[-1] == 2:
        c2+=1
    else:
        c1+=1


save("BP_train", R_train)
save("BP_test", R_test)

print(len(R_train), len(R_test))
print(c0, c1, c2)