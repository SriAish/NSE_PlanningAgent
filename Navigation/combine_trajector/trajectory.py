from calendar import leapdays
import random
from misc import load, save

wh = load("Nav_15_15_30_195")

# sev = load("nav_s_2")
# nn = load("nav_n_2")

severe = load("s_tr")
mild = load("m_tr")
no_nse = load("n_tr")
s = []
m = []
n = []

# i = 0
# for s_t in sev:
#     if i < 35:
#         l = len(wh)
#         wh.add(s_t)
#         if len(wh) > l:
#             s += [s_t]
#             i += 1
#     else:
#         break

# if i < 35:
#     for s_t in severe:
#         if i < 35:
#             l = len(wh)
#             wh.add(s_t)
#             if len(wh) > l:
#                 s += [s_t]
#                 i += 1
#         else:
#             break

# i = 0
# for m_t in mild:
#     if i < 35:
#         l = len(wh)
#         wh.add(m_t)
#         if len(wh) > l:
#             m += [m_t]
#             i += 1
#     else:
#         break

# i = 0
# for n_t in nn:
#     if i < 35:
#         l = len(wh)
#         wh.add(n_t)
#         if len(wh) > l:
#             n += [n_t]
#             i += 1
#     else:
#         break

# if i < 35:
#     for n_t in no_nse:
#         if i < 35:
#             l = len(wh)
#             wh.add(n_t)
#             if len(wh) > l:
#                 n += [n_t]
#                 i += 1
#         else:
#             break

print(len(s), len(m), len(wh+severe+mild+no_nse))
random.shuffle(s)
random.shuffle(m)
random.shuffle(n)

save("Nav_15_15_30_300", wh+severe+mild+no_nse)

# save("s_tr", s)
# save("m_tr", m)
# save("n_tr", n)
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
# for i in range(45, 50, 5):
#     R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
#     save("Nav_15_15_30_"+str(i*3), R)

# i = 28
# R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
# save("BP_15_15_"+str(i), R)