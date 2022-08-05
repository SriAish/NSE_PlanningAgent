from EnvConst import NavigationConstants
from makeFSA import FSAConstants
import sys
import pickle
import itertools
from math import e
from misc import load

class Agent:
    def __init__(self, pi, x):
        self.pi_ = load()
    def NSE_val(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
               
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        t = self.FSA.symbolT(u, s_, a, self.FSA.symbols["severe"])
                        if t != 0:
                            l = self.x_[(u, s)]*self.pi_[(u, s)][a]*self.BP.T(s, a, s_)*t
                            lhs += l
        
        return lhs

    def NSE_val_mild(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
               
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        t = self.FSA.symbolT(u, s_, a, self.FSA.symbols["mild"])
                        if t != 0:
                            l = self.x_[(u, s)]*self.pi_[(u, s)][a]*self.BP.T(s, a, s_)*t
                            lhs += l
        
        return lhs