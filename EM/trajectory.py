import random
from misc import load, save

severe = load("severe_trajectories_lb")
mild = load("mild_trajectories_lb")
no_nse = load("no_nse_trajectories_lb")
s = []
m = []
n = []
for r in severe:
    if len(r) < 999:
        s += [r]

for r in mild:
    if len(r) < 999:
        m += [r]

for r in no_nse:
    if len(r) < 999:
        n += [r]

for i in range(10, 161, 10):
    R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
    save("BP_"+str(i), R)
