from FB import FB
import pickle
# Initial Value
def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
R = load("R1")

states = ['1', '2']
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
        for s in states:
            delta['0'][i][s] = 1/len(states)
            delta['#'][i][s] = 0
        delta['#'][i]['#'] = 1

    for s in states:
        for i in in_sym:
            for s_ in states:
                delta[s][i][s_] = 1/(len(states) + 1)
            delta[s][i]['#'] = 1/(len(states) + 1)

    return delta

def omega_val(states, in_sym, out_sym):
    omega = {}
    omega['#'] = {}
    for s in states:
        omega[s] = {}
        for i in in_sym:
            omega[s][i] = {}
            for o in out_sym:
                omega[s][i][o] = 1/len(out_sym)
    for i in in_sym:
        omega['#'][i] = {}
        for o in out_sym:
            omega['#'][i][o] = 0
        omega['#'][i][2] = 1
    return omega

o_delta = delta_val(states, in_sym)
o_omega = omega_val(states, in_sym, out_sym)

fb = FB(o_delta, o_omega, states, R)

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
    print(itr, diff)
    del fb
    fb = FB(n_delta, n_omega, states, R)
    o_delta = n_delta
    o_omega = n_omega
    del n_delta
    del n_omega
    itr += 1
    

print(o_delta)
print(o_omega)
