import pickle
import numpy as np
import sys

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
R = load("BP_test_15_15_35_set")
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
    # prec = tp/(tp+fp)
    # rec = tp/(tp+fn)

    return cor/tot

file_name = sys.argv[1][sys.argv[1].index("/")+1:]
for i_try in range(20):
    print(sys.argv[1])
    print("states: ", sys.argv[2], "trial: ", i_try)
    delta = load("results/delta/new_" + file_name + "_" + sys.argv[2] + "_" + str(i_try))
    omega = load("results/omega/new_" + file_name + "_" + sys.argv[2] + "_" + str(i_try))

    # for s in delta:
    #     for i in delta[s]:
    #         print(s, i, delta[s][i])
    # print()
    # print(omega)

    fsa = FSA(delta, omega)

    pr = 0

    for r in range(10):
        pr += run_test(R, fsa)

    print("accuracy of:" + "new_" + file_name + "_" + sys.argv[2] + "_" + str(i_try) + ": ", pr/10)
