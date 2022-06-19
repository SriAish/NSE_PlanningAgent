import random
from misc import load, save

severe = load("severe_test")
mild = load("mild_test")
no_nse = load("no_nse_test")
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

random.shuffle(s)
random.shuffle(m)
random.shuffle(n)

# s_train = s[:int(len(s)/2)]
# m_train = m[:int(len(m)/2)]
# n_train = n[:int(len(n)/2)]
# s_test = s[int(len(s)/2):] 
# m_test = m[int(len(m)/2):]
# n_test = n[int(len(n)/2):]
# save("severe_train", s_train)
# save("severe_test", s_test)
# save("mild_train", m_train)
# save("mild_test", m_test)
# save("no_nse_train", n_train)
# save("no_nse_test", n_test)

print(len(s), len(m), len(n))
# R_train = s_train + m_train + n_train
# R_test = s_test + m_test + n_test
# save("BP_train_set", R_train)
# save("BP_test_set", R_test)
R = random.sample(list(s), 114) +  random.sample(list(m), 114) + random.sample(list(n), 114)
save("Test_Data", R)
# print(len(s), len(m), len(n))
# for i in range(10, 121, 10):
#     R = random.sample(list(s), i) +  random.sample(list(m), i) + random.choices(list(n), k=i)
#     save("BP_n_"+str(i), R)
