from operator import le
import random
from misc import load, save

severe = load("nav_s_train")
mild = load("nav_m_train")
no_nse = load("nav_n_train")
s = []
m = []
n = []

k = 900
for r in severe:
    s += [r]

for r in mild:
    m += [r]

siz = []
for r in no_nse:
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
# save("test_eq", random.sample(list(s), 111) + random.sample(list(m), 111) + random.sample(list(n), 222))
# save("nav_s_train", s_train)
# save("nav_s_test", s_test)
# save("nav_m_train", m_train)
# save("nav_m_test", m_test)
# save("nav_n_train", n_train)
# save("nav_n_test", n_test)

# R_train = s_train + m_train + n_train
# R_test = s_test + m_test + n_test
# save("BP_train_15_15_35_set", R_train)
# save("BP_test_15_15_35_set", R_test)
# R = random.sample(list(s), 14) +  random.sample(list(m), 14) + random.sample(list(n), 14)
# save("Valid_Data_15_15", R)
# print(len(s), len(m), len(n))
for i in range(10, 50, 5):
    R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
    save("Nav_15_15_30_"+str(i*3), R)

# i = 28
# R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
# save("BP_15_15_"+str(i), R)
