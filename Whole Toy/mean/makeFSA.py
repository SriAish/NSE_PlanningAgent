import numpy as np

# LABELS
# 0 : b, r, -g
# 1 : b, -r, -g
# 3 : b, -r, g
from actions import Actions 

class FSAConstants:
    def __init__(self, delta, omega):
        # Defining labels 
        self.label = {}
        self.label[(True, False)] = 0
        self.label[(False, False)] = 1
        self.label[(False, True)] = 2

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
        # print(self.symbol)

    def isEnd(self, state):
        return state[0] == (-1, -1)

    def getLabel(self, state, action):
        if self.isEnd(state):
            return self.label[(False, True)]

        if not self.actions.isMoveAction(action):
            return self.label[(False, False)]
        
        if state[3] or not state[2]:
            return self.label[(False, False)]

        if state[4] == 'r':
            return self.label[(True, False)]
        
        if state[4] == 'p':
            return self.label[(False, False)]

    def nextState(self, u, s, a):
        sig = self.getLabel(s, a)

        s = []
        s_pro = []
        li = []
        for i in self.state_transitions[u][sig]:
            li += [(i, self.state_transitions[u][sig][i])]
        return li

    def symbolT(self, u, s, a, sym):
        # print("get symbol:", s)
        sig = self.getLabel(s, a)
        return self.symbol[u][sig][sym]

    def T(self, u, s, a, u_):
        sig = self.getLabel(s, a)
        return self.state_transitions[u][sig][u_]

    def transition(self, u, a, s):
        sig = self.getLabel(s, a)
        s = []
        pr = []
        for u_ in self.state_transitions[u][sig]:
            s += [u_]
            pr += [self.state_transitions[u][sig][u_]]

        sy = []
        sy_pr = []
        for sy_ in self.symbol[u][sig]:
            sy += [sy_]
            sy_pr += [self.symbol[u][sig][sy_]]
        # print(pr)
        if sum(sy_pr) == 0:
            sy_pr[2] = 1
        # print(u, sig, sy, sy_pr)
        return np.random.choice(s, p=pr), np.random.choice(sy, p=sy_pr)

if __name__ == '__main__':
    fsa = FSAConstants(delta, omega)
    # trace = ((((0, 0), (5, 4), False, 'p'), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'left'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'right'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((5, 3), (5, 4), False, 'p', 2), 'right'), (((5, 4), (5, 4), False, 'p', 2), 'pick_up'), (((5, 4), (5, 4), True, 'p', 2), 'up'), (((5, 5), (5, 5), True, 'p', 2), 'up'), (((4, 5), (4, 5), True, 'p', 2), 'up'), (((4, 6), (4, 6), True, 'p', 2), 'up'), (((3, 6), (3, 6), True, 'p', 2), 'drop'))
    # trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'down'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((4, 4), (5, 4), False, 'r', 3), 'down'), (((5, 4), (5, 4), False, 'p', 3), 'pick_up'), (((5, 4), (5, 4), True, 'p', 3), 'up'), (((4, 4), (4, 4), True, 'r', 4), 'up'), (((3, 4), (3, 4), True, 'r', 5), 'right'), (((3, 5), (3, 5), True, 'p', 5), 'right'), (((3, 6), (3, 6), True, 'p', 5), 'drop'), 'end')

    u = ((0, 0), (1, 1), False, False, 'p')
    print(fsa.nextState('0', u, "down"))