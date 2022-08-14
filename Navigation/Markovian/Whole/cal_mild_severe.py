from symtable import Symbol
from EnvConst import NavigationConstants
from makeFSA import FSAConstants
import sys
import pickle
import itertools
from math import e
from misc import load

class Agent:
    def __init__(self, BP, FSA):
        self.pi_ = load("policy/FSA_LP_p_Nav_pol_45_6.pkl")
        self.x_ = load("policy/FSA_LP_x_Nav_pol_45_6.pkl")
        self.BP = BP
        self.FSA = FSA

    def NSE_val(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
                
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if s[0] == (14,14) and s[1] == 'fast' and u == '5' and s_[0] == (-1, -1):
                        print("initial state: ", u, s)
                        print("next state: ", s_)
                        print(self.BP.T(s, a, s_))
                        print(self.FSA.getLabel(s_, a))
                        la = self.FSA.getLabel(s_, a)
                        print(self.FSA.symbol[u])
                        print(self.FSA.symbolT(u, s_, a, self.FSA.symbols["severe"]))
                        print(self.FSA.symbolT(u, s_, a, 'S', True))
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


g_pos = (int(sys.argv[2]), int(sys.argv[3]))
g_state = [(g_pos, 'fast', False, False), (g_pos, 'slow', False, False)]
ped = [(0, 12),(0, 13),(0, 14), (4, 0),(4, 1),(4, 5),(4, 6),(4, 7),(4, 8),(5, 9),(5, 10),(7, 0),(7, 1),(7, 10),(7, 11),(10, 0),(10, 1),(10, 2),(10, 3),(10, 9),(10, 10),(10, 11),(10, 12),(10, 13),(10, 14),(11, 0),(11, 1),(11, 2),(11, 3),(11, 5),(11, 6),(11, 7),(11, 8),(11, 9),(11, 10),(11, 11),(11, 12),(11, 13),(11, 14)]
pud = [(0, 3),(0, 4),(0, 5),(0, 6),(4, 2),(4, 3),(4, 4),(4, 9),(5, 0),(5, 1),(5, 2),(7, 2),(7, 7),(7, 8),(7, 9),(11, 4)]
# ped = [(1, 0)]
# pud = [(0, 2)]
BP = NavigationConstants(int(sys.argv[1]), ped, pud, g_state)
file_name = sys.argv[4][sys.argv[4].index("/")+1:]
# file_name = sys.argv[12][sys.argv[12].index("/")+1:]
delta = load("results/delta/new_" + file_name + "_" + sys.argv[5] + "_best")
omega = load("results/omega/new_" + file_name + "_" + sys.argv[5] + "_best")
FSA = FSAConstants(delta, omega)
a = Agent(BP, FSA)
print(a.NSE_val())