from operator import le
import random
from misc import load, save

s = list(load("n_2_4_8"))
n = list(load("nn_2_4_8"))

print(len(s), len(n))
random.shuffle(s)
# random.shuffle(m)
random.shuffle(n)

t_train = s + n

save("Toy_train_data_2_4", t_train)

# i = 28
# R = random.sample(list(s), i) +  random.sample(list(m), i) + random.sample(list(n), i)
# save("BP_15_15_"+str(i), R)
