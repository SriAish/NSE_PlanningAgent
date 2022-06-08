from FB import FB
import sys
import pickle
from misc import load, init_delta, init_omega, objective, cal_delta, cal_omega
# Initial Value
# severe = load("severe_trajectories_lb")
# mild = load("mild_trajectories_lb")
# no_nse = load("no_nse_trajectories_lb")
# R_ = severe + mild + no_nse
R = load("R2_train")
# for r in R_:
#     if len(r) < 999:
#         R += [r]

states = ['1', '2', '3', '4', '5', '6', '7', '8']
in_sym = ['a', 'b', 'e']
out_sym = [0, 1, 2]

o_delta = init_delta(states, in_sym)
o_omega = init_omega(states, in_sym, out_sym)

fb = FB(o_delta, o_omega, states, R)

diff = 1
itr = 0
o_obj = objective(fb, states, in_sym, out_sym, o_delta, o_omega)

objective_val = []
objective_val.append(o_obj)
while diff > 0.0001:
    n_delta = cal_delta(fb, states, in_sym)
    n_omega = cal_omega(fb, states, in_sym, out_sym)

    diff = 0
    for i in n_delta:
        for j in n_delta[i]:
            for k in n_delta[i][j]:
                diff += abs(n_delta[i][j][k]-o_delta[i][j][k])

    for i in n_omega:
        for j in n_omega[i]:
            for k in n_omega[i][j]:
                diff += abs(n_omega[i][j][k]-o_omega[i][j][k])

    del fb
    fb = FB(n_delta, n_omega, states, R)
    o_delta = n_delta
    o_omega = n_omega
    del n_delta
    del n_omega
    o_obj = objective(fb, states, in_sym, out_sym, o_delta, o_omega)
    print(itr, diff)
    sys.stdout.flush()
    objective_val.append(o_obj)
    itr += 1
    
print(o_delta)
print(o_omega)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

save("obj_R2", objective_val)
save("delta_R2", o_delta)
save("omega_R2", o_omega)
