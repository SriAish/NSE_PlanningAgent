from FB import FB
import pickle
import random
from math import log
import sys

# Initial Value
def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
R = load("R3_train")

states = ['1', '2', '3']
in_sym = ['a', 'b', 'e']
out_sym = [0, 1, 2]

def delta_val(states, in_sym):
    delta = {}

    delta['0'] = {}
    for s in states:
        delta[s] = {}
    delta['#'] = {}

    for i in in_sym:
        delta['0'][i] = {}
        delta['#'][i] = {}
        for s in states:
            delta[s][i] = {}
        
    for i in in_sym:
        sum_del = 0
        for s in states:
            delta['0'][i][s] = random.random()
            sum_del += delta['0'][i][s]
            delta['#'][i][s] = 0
        for s in states:
            delta['0'][i][s] = (delta['0'][i][s]/sum_del)
        delta['#'][i]['#'] = 1

    for s in states:
        for i in in_sym:
            sum_del = 0
            for s_ in states:
                delta[s][i][s_] = random.random()
                sum_del += delta[s][i][s_]
            delta[s][i]['#'] = random.random()
            sum_del += delta[s][i]['#']
            delta[s][i]['#'] = delta[s][i]['#']/sum_del
            for s_ in states:
                delta[s][i][s_] = delta[s][i][s_]/sum_del

    return delta

def omega_val(states, in_sym, out_sym):
    omega = {}
    omega['#'] = {}
    for s in states:
        omega[s] = {}
        for i in in_sym:
            omega[s][i] = {}
            sum_omega = 0
            for o in out_sym:
                omega[s][i][o] = random.random()
                sum_omega += omega[s][i][o]
            for o in out_sym:
                omega[s][i][o] = omega[s][i][o]/sum_omega
    for i in in_sym:
        omega['#'][i] = {}
        for o in out_sym:
            omega['#'][i][o] = 0
        omega['#'][i][2] = 1
    return omega

o_delta = delta_val(states, in_sym)
o_omega = omega_val(states, in_sym, out_sym)

fb = FB(o_delta, o_omega, states, R)

# Calculate Objective:
def objective(fb, states, in_sym, out_sym, delta, omega):
    # Part 1
    p1 = 0
    for s in states:
        for i in in_sym:
            v1 = 0
            for r in range(len(R)):
                if R[r][0] == i:
                    v1 += fb.gamma(r, 0, s)
            if delta['0'][i][s] != 0:
                p1 += v1*log(delta['0'][i][s])

    # Part 2
    p2 = 0
    for s in states:
        for i in in_sym:
            for s_ in states:
                v2 = 0
                for r in range(len(R)):
                    for t in range(len(R[r]) - 3):
                        if R[r][t+1] == i:
                            v2 += fb.eta(r, t, s, s_)
                if delta[s][i][s_] != 0:
                    p2 += v2*log(delta[s][i][s_])

    # Part 3
    p3 = 0
    for s in states:
        for i in in_sym:
            v3 = 0
            for r in range(len(R)):
                t = len(R[r]) - 3
                if R[r][t+1] == i:
                    v3 += fb.gamma(r, t, s)
            if delta[s][i]['#'] != 0:
                p3 += v3*log(delta[s][i]['#'])

    # Part 4
    p4 = 0
    for s in states:
        for i in in_sym:
            for o in out_sym:
                v4 = 0
                for r in range(len(R)):
                    t = len(R[r]) - 3
                    if R[r][t+1] == i and R[r][t+2] == o:
                        v4 += fb.gamma(r, t, s)
                if omega[s][i][o] != 0:
                    p4 += v4*log(omega[s][i][o])
                
    return p1+p2+p3+p4

# EM-Step
def cal_delta(fb, states, in_sym):
    delta = {}

    delta['0'] = {}
    delta['#'] = fb.delta['#']
    for i in in_sym:
        delta['0'][i] = {}
        for s in states:
            num = 0
            den = 0
            for r in range(len(R)):
                if R[r][0] == i:
                    den += 1
                    num += fb.gamma(r, 0, s)
            if num == 0:
                delta['0'][i][s] = 0
            else:
                delta['0'][i][s] = num/den

    den = {}
    for m in states:
        delta[m] = {}
        for i in in_sym:
            delta[m][i] = {}
            den[(m, i)] = 0
            for o in states:
                for r in range(len(R)):
                    for t in range(len(R[r]) - 3):
                        if R[r][t+1] == i:
                            den[(m, i)] += fb.eta(r, t, m, o)

            num = 0
            for r in range(len(R)):
                t = len(R[r]) - 3
                if R[r][t+1] == i:
                    num += fb.gamma(r, t, m)
            den[(m, i)] += num

            if num == 0:
                delta[m][i]['#'] = 0
            else:
                delta[m][i]['#'] = num/den[(m, i)]

    for s in states:
        for i in in_sym:
            for s_ in states:
                num = 0
                for r in range(len(R)):
                    for t in range(len(R[r]) - 3):
                        if R[r][t+1] == i:
                            num += fb.eta(r, t, s, s_)
                if num == 0:
                    delta[s][i][s_] = 0
                else:
                    delta[s][i][s_] = num/den[(s, i)]


    return delta

def cal_omega(fb, states, in_sym, out_sym):
    omega = {}
    omega['#'] = fb.omega['#']

    for s in states:
        omega[s] = {}
        for i in in_sym:
            omega[s][i] = {}
            num = {}
            den = 0
            for o in out_sym:
                num[o] = 0
                for r in range(len(R)):
                    t = len(R[r]) - 3
                    if R[r][t+2] == o:
                        if R[r][t+1] == i:
                            num[o] += fb.gamma(r, t, s)
                den += num[o]
            for o in out_sym:
                if num[o] == 0:
                    omega[s][i][o] = 0
                else:
                    omega[s][i][o] = num[o]/den
    return omega
diff = 1
itr = 0
o_obj = objective(fb, states, in_sym, out_sym, o_delta, o_omega)

objective_val = []
objective_val.append(o_obj)
while diff > 0.001:
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

save("obj_R3", objective_val)
save("delta_R3", o_delta)
save("omega_R3", o_omega)
