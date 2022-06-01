from FB import FB
import pickle
import random
from math import log
import sys
import numpy as np

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
R = load("R3_test")

delta = load("delta_R3")
omega = load("omega_R3")

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
                    self.omega[s][i].append(s_)
                    self.omega_val[s][i].append(policy[s][i][s_])
                    # self.delta_val[s][i].append(

    def getNextState(self, state, i):
        return np.random.choice(self.delta[state][i], p = self.delta_val[state][i])

    def getOutSym(self, state, i):
        return np.random.choice(self.omega[state][i], p = self.omega_val[state][i])

def run_test(R, fsa):
    cor = 0
    in_cor = 0
    for r in R:
        st = '0'
        for t in range(len(r)-2):
            st = fsa.getNextState(st, r[t])
        out = fsa.getOutSym(st, r[len(r)-2])
        if out == r[len(r)-1]:
            cor += 1
        else:
            in_cor += 1

    tot = cor + in_cor

    return cor/tot, in_cor/tot

fsa = FSA(delta, omega)
print(run_test(R, fsa))
