import pickle
import sys


def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)
delta = load("delta")
omega = load("omega")

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
        self.symbols["empty"] = 'E'

        # Symbol transiyion
        self.symbol = {}
        self.symbol["u0"] = {}
        self.symbol["u1"] = {}
        self.symbol["u2"] = {}
        self.symbol["u3"] = {}
        self.symbol["u4"] = {}
        self.symbol["u5"] = {}
        self.symbolTransition()

    def isEnd(self, state):
        return state[0] == (-1, -1)

    def symbolTransition(self):
        self.symbol["u0"][0] = self.symbols["empty"]
        self.symbol["u0"][1] = self.symbols["empty"]
        self.symbol["u0"][2] = self.symbols["empty"]

        self.symbol["u1"][0] = self.symbols["empty"]
        self.symbol["u1"][1] = self.symbols["empty"]
        self.symbol["u1"][2] = self.symbols["no_nse"]

        self.symbol["u2"][0] = self.symbols["empty"]
        self.symbol["u2"][1] = self.symbols["empty"]
        self.symbol["u2"][2] = self.symbols["mild"]

        self.symbol["u3"][0] = self.symbols["empty"]
        self.symbol["u3"][1] = self.symbols["empty"]
        self.symbol["u3"][2] = self.symbols["mild"]

        self.symbol["u4"][0] = self.symbols["empty"]
        self.symbol["u4"][1] = self.symbols["empty"]
        self.symbol["u4"][2] = self.symbols["severe"]

        self.symbol["u5"][0] = self.symbols["empty"]
        self.symbol["u5"][1] = self.symbols["empty"]
        self.symbol["u5"][2] = self.symbols["empty"]

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


    def getSymbol(self, state, label):
        # print(state, label, self.symbol[state][label])
        return self.symbol[state][label]

    def symbolT(self, u, s, a, sym):
        # print("get symbol:", s)
        symbol = self.getSymbol(u, self.getLabel(s, a))

        if sym == symbol:
            return 1
        return 0

    def T(self, u, s, a, u_):
        sig = self.getLabel(s, a)
        return self.state_transitions[u][sig][u_]


if __name__ == '__main__':
    fsa = FSAConstants(delta, omega)
    # trace = ((((0, 0), (5, 4), False, 'p'), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'left'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'right'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((5, 3), (5, 4), False, 'p', 2), 'right'), (((5, 4), (5, 4), False, 'p', 2), 'pick_up'), (((5, 4), (5, 4), True, 'p', 2), 'up'), (((5, 5), (5, 5), True, 'p', 2), 'up'), (((4, 5), (4, 5), True, 'p', 2), 'up'), (((4, 6), (4, 6), True, 'p', 2), 'up'), (((3, 6), (3, 6), True, 'p', 2), 'drop'))
    # trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'down'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((4, 4), (5, 4), False, 'r', 3), 'down'), (((5, 4), (5, 4), False, 'p', 3), 'pick_up'), (((5, 4), (5, 4), True, 'p', 3), 'up'), (((4, 4), (4, 4), True, 'r', 4), 'up'), (((3, 4), (3, 4), True, 'r', 5), 'right'), (((3, 5), (3, 5), True, 'p', 5), 'right'), (((3, 6), (3, 6), True, 'p', 5), 'drop'), 'end')

    u = ((1, 1), (1, 1), True, False, 'r')
    print(fsa.T("u1", u, "u2"))