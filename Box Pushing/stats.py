import pickle
import numpy as np
import sys

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
R = load("new_test")
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

def F1_score(R, out_sym, o):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(len(out_sym)):
        if R[i][-1] == out_sym[i]:
            if out_sym[i] == o:
                tp += 1
            else:
                tn += 1 
        else:
            if out_sym[i] == o:
                fp += 1
            else:
                fn += 1
    
    prec = float(tp)/float(tp + fp)
    rec = float(tp)/float(tp + fn)
    return (2*prec*rec)/(prec + rec)

def run_test(R, fsa):
    out_sym = []
    for r in R:
        st = '0'
        for t in range(len(r)-2):
            st = fsa.getNextState(st, r[t])
        out_sym += [fsa.getOutSym(st, r[len(r)-2])]
    print("f1 score: N, ", F1_score(R, out_sym, 'N'), "M, ", F1_score(R, out_sym, 'M'), "S, ", F1_score(R, out_sym, 'S'))

file_name = sys.argv[1][sys.argv[1].index("/")+1:]
# for i_try in range(10):
print(sys.argv[1])
# print("states: ", sys.argv[2], "trial: ", i_try)
delta = load("results/delta/new_" + file_name + "_" + sys.argv[2] + "_best")
omega = load("results/omega/new_" + file_name + "_" + sys.argv[2] + "_best")

fsa = FSA(delta, omega)

print("new_" + file_name + "_" + sys.argv[2] + "_" + "best" + ": ", run_test(R, fsa))
