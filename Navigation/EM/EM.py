from FB import FB
import sys
import pickle
import random
from misc import load, save
from math import log
import time

R = load(sys.argv[1])

# for r in R:
#     if r[-1] == 'M':
#         print(r)
# print(R)
# R = random.sample(list(R_), 30)

print(len(R))
def init_delta(states, in_sym):
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

def init_omega(states, in_sym, out_sym):
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
        omega['#'][i][3] = 1
    return omega

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

states = []
for i in range(int(sys.argv[2])):
 states += [str(i+1)]
in_sym = [0, 1, 2, 3, 4, 5, 6]
out_sym = ['N', 'S', 'M', 3]

file_name = sys.argv[1][sys.argv[1].index("/")+1:]

all_start_time = time.time()
trial_seed = {}
for i_try in range(1):
    r_seed = random.randint(i_try, (1+i_try)*(2+i_try))
    random.seed(r_seed)
    trial_seed[i_try] = r_seed
    print(sys.argv[1])
    print("states: ", sys.argv[2], "trial: ", i_try)
    start_time = time.time()
    file_name = sys.argv[3][sys.argv[3].index("/")+1:]
    o_delta = load("results/delta/new_" + file_name + "_" + sys.argv[4] + "_best")
    o_omega = load("results/omega/new_" + file_name + "_" + sys.argv[4] + "_best")
    # o_delta = init_delta(states, in_sym)
    # o_omega = init_omega(states, in_sym, out_sym)

    fb = FB(o_delta, o_omega, states, R)

    diff = 1
    itr = 0
    o_obj = objective(fb, states, in_sym, out_sym, o_delta, o_omega)
    save("results/delta/init_" + file_name + "_" + sys.argv[2] + "_" + str(i_try), o_delta)
    save("results/omega/init_" + file_name + "_" + sys.argv[2] + "_" + str(i_try), o_omega)
    objective_val = []
    objective_val.append(o_obj)
    print(1)
    while diff > 0.005:
        n_delta = cal_delta(fb, states, in_sym)
        n_omega = cal_omega(fb, states, in_sym, out_sym)
        print(1)

        diff = 0
        # for i in n_delta:
        #     for j in n_delta[i]:
        #         for k in n_delta[i][j]:
        #             diff += abs(n_delta[i][j][k]-o_delta[i][j][k])

        # for i in n_omega:
        #     for j in n_omega[i]:
        #         for k in n_omega[i][j]:
        #             diff += abs(n_omega[i][j][k]-o_omega[i][j][k])

        del fb
        fb = FB(n_delta, n_omega, states, R)
        o_delta = n_delta
        o_omega = n_omega
        del n_delta
        del n_omega
        print(1)
    
        n_obj = objective(fb, states, in_sym, out_sym, o_delta, o_omega)
        diff = abs(n_obj - o_obj)
        # print(itr, diff)
        sys.stdout.flush()
        o_obj = n_obj
        print(1)

        objective_val.append(o_obj)
        itr += 1
    print(itr)
    print("done")
    file_name = sys.argv[1][sys.argv[1].index("/")+1:]
    save("results/objective/new_ch_" + file_name + "_" + sys.argv[2] + "_" + str(i_try), objective_val)
    save("results/seed/seed_ch_" + file_name + "_" + sys.argv[2] + "_" + str(i_try), trial_seed)
    save("results/delta/new_ch_" + file_name + "_" + sys.argv[2] + "_" + str(i_try), o_delta)
    save("results/omega/new_ch_" + file_name + "_" + sys.argv[2] + "_" + str(i_try), o_omega)

    print("--- %s seconds ---" % (time.time() - start_time))

print("--- %s seconds for all trials---" % (time.time() - all_start_time))
print("========================================================")