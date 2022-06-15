import random
from misc import load, save



severe = load("severe_train")
mild = load("mild_train")
no_nse = load("no_nse_train")
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

print(len(s), len(m), len(n))
# R = list(s) + list(m) + list(n)
# save("BP_whole_set", R)

# print(len(s), len(m), len(n))
for i in range(10, 114, 20):
    R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
    save("BP_wh_"+str(i), R)
