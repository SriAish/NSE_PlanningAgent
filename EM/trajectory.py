import random
from misc import load, save

severe = load("Test_Data")
mild = load("Test_Data2")
no_nse = load("Test_Data_15_15")
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

# random.shuffle(s)
# random.shuffle(m)
# random.shuffle(n)

# save("severe_wh_test", s)
# save("mild_wh_test", m)
# save("no_nse_wh_test", n)
# s_train = s[:int(len(s)/2)]
# m_train = m[:int(len(m)/2)]
# n_train = n[:int(len(n)/2)]
# s_test = s[int(len(s)/2):] 
# m_test = m[int(len(m)/2):]
# n_test = n[int(len(n)/2):]
# save("severe_valid_15_15", s_train)
# save("severe_test_15_15", s_test)
# save("mild_valid_15_15", m_train)
# save("mild_test_15_15", m_test)
# save("no_nse_valid_15_15", n_train)
# save("no_nse_test_15_15", n_test)

print(len(s), len(m), len(n))
# R_train = s_train + m_train + n_train
# R_test = s + m + n
# save("BP_train_set", R_train)
# save("BP_test_set", R_test)
# R = random.sample(list(s), 14) +  random.sample(list(m), 14) + random.sample(list(n), 14)
# save("Valid_Data_15_15", R)
# print(len(s), len(m), len(n))
# for i in range(10, 21, 10):
#     R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
#     save("BP_15_15_"+str(i), R)

# i = 28
# R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
# save("BP_15_15_"+str(i), R)
