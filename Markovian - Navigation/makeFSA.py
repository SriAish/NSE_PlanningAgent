import numpy as np
import sys
from misc import load

# LABELS
# 0 : b, r, -g
# 1 : b, -r, -g
# 3 : b, -r, g
from actions import Actions 

class FSAConstants:
    def __init__(self, delta, omega):
        # Defining labels 
        self.label = {}
        self.label[(False, False, False, False)] = 0
        self.label[(True, False, False, False)] = 1
        self.label[(False, False, True, False)] = 2
        self.label[(True, False, True, False)] = 3
        self.label[(False, True, True, False)] = 4
        self.label[(True, True, True, False)] = 5
        self.label[(False, False, False, True)] = 6

        # Defining states
        self.states = []
        for i in delta:
            self.states.append(i)

         # Sstting up the actions
        self.actions = Actions()

        # Defining state transitions
        self.state_transitions = delta
        for i in self.label:
            self.state_transitions['0'][self.label[i]]['#'] = 0
            for s in self.states:
                self.state_transitions[s][self.label[i]]['0'] = 0
        print(self.state_transitions)

        # Symbol Definition
        self.symbols = {}

        self.symbols["severe"] = 'S'
        self.symbols["mild"] = 'M'
        self.symbols["no_nse"] = 'N'
        self.symbols["empty"] = 3

        # Symbol transiyion
        self.symbol = omega
        self.symbol['0'] = {}
        for i in self.label:
            self.symbol['0'][self.label[i]] = {}
            for o in self.symbols:
                self.symbol['0'][self.label[i]][self.symbols[o]] = 0
        print(self.symbol)

    def isEnd(self, state):
        return state[0] == (-1, -1)

    def getLabel(self, state, action):
        if self.isEnd(state):
            return self.label[(False, False, False, True)]
        fast = True
        if state[1] == 'slow':
            fast = False

        return self.label[(fast, state[2], state[3], False)]

    def nextState(self, u, s, a):
        sig = self.getLabel(s, a)

        li = []
        for i in self.state_transitions[u][sig]:
            li += [(i, self.state_transitions[u][sig][i])]
        return li

    def symbolT(self, u, s, a, sym, pr = False):
        # print("get symbol:", s)
        sig = self.getLabel(s, a)
        if pr:
            print(u, sig, sym)
        return self.symbol[u][sig][sym]

    def T(self, u, s, a, u_):
        sig = self.getLabel(s, a)
        return self.state_transitions[u][sig][u_]


if __name__ == '__main__':
    file_name = sys.argv[4][sys.argv[4].index("/")+1:]
    delta = load("results/delta/new_" + file_name + "_" + sys.argv[5] + "_best")
    omega = load("results/omega/new_" + file_name + "_" + sys.argv[5] + "_best")
    fsa = FSAConstants(delta, omega)
    # trace = ((((0, 0), (5, 4), False, 'p'), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'left'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'right'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((5, 3), (5, 4), False, 'p', 2), 'right'), (((5, 4), (5, 4), False, 'p', 2), 'pick_up'), (((5, 4), (5, 4), True, 'p', 2), 'up'), (((5, 5), (5, 5), True, 'p', 2), 'up'), (((4, 5), (4, 5), True, 'p', 2), 'up'), (((4, 6), (4, 6), True, 'p', 2), 'up'), (((3, 6), (3, 6), True, 'p', 2), 'drop'))
    # trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'down'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((4, 4), (5, 4), False, 'r', 3), 'down'), (((5, 4), (5, 4), False, 'p', 3), 'pick_up'), (((5, 4), (5, 4), True, 'p', 3), 'up'), (((4, 4), (4, 4), True, 'r', 4), 'up'), (((3, 4), (3, 4), True, 'r', 5), 'right'), (((3, 5), (3, 5), True, 'p', 5), 'right'), (((3, 6), (3, 6), True, 'p', 5), 'drop'), 'end')

    u = ((-1, -1), 'fast', False, False)
    print(fsa.symbolT('5', u, "down", 'S'))