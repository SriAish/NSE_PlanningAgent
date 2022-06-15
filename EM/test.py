import pickle
import numpy as np

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
# severe = load("severe_trajectories_lb")
# mild = load("mild_trajectories_lb")
# no_nse = load("no_nse_trajectories_lb")
# R = load("BP_test")
R = load("BP_wh_220")
print(len(R))

# rn = 0
# rs =0
# rm =0
# for r in R:
#     if r[-1] == 'N':
#         rn+=1
#     if r[-1] == 'S':
#         rs +=1
#     if r[-1] == 'M':
#         rm +=1

# print(rs, rn, rm)
delta = load("delta_BP10")
omega = load("omega_BP10")

for s in delta:
    for i in delta[s]:
        print(s, i, delta[s][i])
print()
print(omega)
class FSA:
    def __init__(self, delta, omega):
        self.loadDelta(delta)
        self.loadOmega(omega)

    def loadDelta(self, name):
        policy = name
        self.delta = {}
        self.delta_val = {}
        for s in policy:
            self.delta[s] = {}
            self.delta_val[s] = {}
            for i in policy[s]:
                self.delta[s][i] = []
                self.delta_val[s][i] = []
                for s_ in policy[s][i]:
                    self.delta[s][i].append(s_)
                    self.delta_val[s][i].append(policy[s][i][s_])
                    # self.delta_val[s][i].append(round(policy[s][i][s_], 5))
    
    def loadOmega(self, name):
        policy = name
        self.omega = {}
        self.omega_val = {}
        for s in policy:
            self.omega[s] = {}
            self.omega_val[s] = {}
            for i in policy[s]:
                self.omega[s][i] = []
                self.omega_val[s][i] = []
                for s_ in policy[s][i]:
                    # print(s, i, s_)
                    self.omega[s][i].append(s_)
                    self.omega_val[s][i].append(policy[s][i][s_])
                    # self.delta_val[s][i].append(

    def getNextState(self, state, i):
        # print("state:", state, i, self.delta_val[state][i])
        return np.random.choice(self.delta[state][i], p = self.delta_val[state][i])

    def getOutSym(self, state, i):
        # print("out:", state, i, self.omega[state][i], self.omega_val[state][i])
        return np.random.choice(self.omega[state][i], p = self.omega_val[state][i])

def run_test(R, fsa):
    cor = 0
    in_cor = 0
    tp = 0.0
    tn = 0.0
    fp = 0.0
    fn = 0.0
    for r in R:
        st = '0'
        for t in range(len(r)-2):
            st = fsa.getNextState(st, r[t])
        out = fsa.getOutSym(st, r[len(r)-2])
        if out == r[-1]:
            if out == 0:
                tn += 1
            else:
                tp += 1
            cor += 1
        else:
            # print(out)
            if out == 0:
                fn += 1
            else:
                fp += 1
            in_cor += 1
            # print(r)

    tot = cor + in_cor
    # print(cor, tp, fp, fn)
    prec = tp/(tp+fp)
    rec = tp/(tp+fn)

    return cor/tot, in_cor/tot, "precision: ", prec, "recall: ", rec, "F1 Score", ((2*prec*rec)/(prec + rec))

fsa = FSA(delta, omega)

for r in range(1):
    print(run_test(R, fsa))
