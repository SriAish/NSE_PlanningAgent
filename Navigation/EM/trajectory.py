from operator import le
import random
from misc import load, save

severe = load("s_nav_15_15_25")
mild = load("m_nav_15_15_25")
no_nse = load("n_nav_15_15_25")
s = []
m = []
n = []

k = 900
for r in severe:
    if len(r) < 32:
        if list(r).count(2) > 1 or list(r).count(3) > 1: 
                s += [r]
        elif k > 0 and len(r) < 15:
            s += [r]
            k -= 1

for r in mild:
    if len(r) > 15 and len(r) < 25:
        m += [r]

siz = []
for r in no_nse:
    if len(r) > 12 and len(r) < 14:
        if list(r).count(0) < 5: 
            n += [r]

print(len(s), len(m), len(n))
random.shuffle(s)
random.shuffle(m)
random.shuffle(n)

# save("nav_s", s)
# save("nav_m", m)
# save("nav_n", n)
# s_train =  s[:int(len(s)*0.8)]
# m_train = m[:int(len(m)*0.8)]
# n_train = n[:int(len(n)*0.8)]
# s_test = s[int(len(s)*0.8):]
# m_test = m[int(len(m)*0.8):]
# n_test = n[int(len(n)*0.8):]
# save("test_wh", n+s+m)
# save("test_eq", random.sample(list(s), 385) + random.sample(list(n), 385) + random.sample(list(n), 385))
# save("s_nav_15_15_25", s_train)
# save("s_nav_test_15_15_25", s_test)
# save("m_nav_15_15_25", m_train)
# save("m_nav_test_15_15_25", m_test)
# save("n_nav_15_15_25", n_train)
# save("n_nav_test_15_15_25", n_test)

# R_train = s_train + m_train + n_train
# R_test = s_test + m_test + n_test
# save("BP_train_15_15_35_set", R_train)
# save("BP_test_15_15_35_set", R_test)
# R = random.sample(list(s), 14) +  random.sample(list(m), 14) + random.sample(list(n), 14)
# save("Valid_Data_15_15", R)
# print(len(s), len(m), len(n))
for i in range(45, 50, 5):
    R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
    save("Nav_15_15_30_"+str(i*3), R)

# i = 28
# R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
# save("BP_15_15_"+str(i), R)
