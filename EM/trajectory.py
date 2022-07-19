from operator import le
import random
from misc import load, save

severe = load("BP_test_15_15_35_set")
print(len(severe))
mild = load("m_train_15_15_35")
no_nse = load("nn_train_15_15_35")
s = []
m = []
n = []

for r in severe:
    if len(r) < 999:
        s += [r]

for r in mild:
    if len(r) < 999:
        m += [r]

siz = []
for r in no_nse:
    if len(r) <= 999:
        n += [r]

print(len(s), len(m), len(n))
# random.shuffle(s)
# random.shuffle(m)
# random.shuffle(n)

# save("severe_wh_test", s)
# save("mild_wh_test", m)
# save("no_nse_wh_test", n)
# s_train =  s[:int(len(s)*0.8)]
# m_train = m[:int(len(m)*0.8)]
# n_train = n[:int(len(n)*0.8)]
# s_test = s[int(len(s)*0.8):]
# m_test = m[int(len(m)*0.8):]
# n_test = n[int(len(n)*0.8):]
# save("s_train_15_15_35", s_train)
# save("s_test_15_15_35", s_test)
# save("m_train_15_15_35", m_train)
# save("m_test_15_15_35", m_test)
# save("nn_train_15_15_35", n_train)
# save("nn_test_15_15_35", n_test)

# R_train = s_train + m_train + n_train
# R_test = s_test + m_test + n_test
# save("BP_train_15_15_35_set", R_train)
# save("BP_test_15_15_35_set", R_test)
# R = random.sample(list(s), 14) +  random.sample(list(m), 14) + random.sample(list(n), 14)
# save("Valid_Data_15_15", R)
# print(len(s), len(m), len(n))
for i in range(15, 26, 5):
    R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
    save("BP_15_15_35_"+str(i), R)

# i = 28
# R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
# save("BP_15_15_"+str(i), R)
