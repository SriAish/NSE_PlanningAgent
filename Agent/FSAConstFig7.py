# LABELS
# 0 : b, r0, -r1, -r2, -g
# 1 : b, -r0, r1, -r2, -g
# 2 : b, -r0, -r1, r2, -g
# 3 : b, -r0, -r1, -r2, -g
# 4 : b, r0, -r1, -r2, g
# 5 : b, -r0, r1, -r2, g
# 6 : b, -r0, -r1, r2, g
# 7 : b, -r0, -r1, -r2, g

import sys

class FSAConstants:
    def __init__(self, goal = ()):
        # Defining labels 
        self.label = {}
        self.label[(True, False, False, False)] = 0
        self.label[(False, True, False, False)] = 1
        self.label[(False, False, True, False)] = 2
        self.label[(False, False, False, False)] = 3
        self.label[(True, False, False, True)] = 4
        self.label[(False, True, False, True)] = 5
        self.label[(False, False, True, True)] = 6
        self.label[(False, False, False, True)] = 7

        # Defining states
        self.states = ["u0", "u1", "u2", "u3", "u4", "u5"]

        # Defining state transitions
        self.state_transitions = {}
        self.state_transitions["u0"] = {}
        self.state_transitions["u1"] = {}
        self.state_transitions["u2"] = {}
        self.state_transitions["u3"] = {}
        self.state_transitions["u4"] = {}
        self.state_transitions["u5"] = {}

        self.stateTransition()

        # Storing transition probabilities
        self.transition_probabilities = {}

        # MDP end state
        self.goal = goal


        # Symbol Definition
        self.symbols = {}

        self.symbols["severe"] = 'S'
        self.symbols["mild"] = 'M'
        self.symbols["no_nse"] = 'N'
        self.symbols["empty"] = 'E'

    def isEnd(self, state):
        return state[0] == self.goal and state[1] == self.goal

    def stateTransition(self):
        self.state_transitions["u0"][0] = "u1"
        self.state_transitions["u0"][1] = "u2"
        self.state_transitions["u0"][2] = "u0"
        self.state_transitions["u0"][3] = "u0"
        self.state_transitions["u0"][4] = "u0"
        self.state_transitions["u0"][5] = "u0"
        self.state_transitions["u0"][6] = "u0"
        self.state_transitions["u0"][7] = "u0"

        self.state_transitions["u1"][0] = "u1"
        self.state_transitions["u1"][1] = "u2"
        self.state_transitions["u1"][2] = "u1"
        self.state_transitions["u1"][3] = "u1"
        self.state_transitions["u1"][4] = "u5"
        self.state_transitions["u1"][5] = "u1"
        self.state_transitions["u1"][6] = "u1"
        self.state_transitions["u1"][7] = "u1"

        self.state_transitions["u2"][0] = "u2"
        self.state_transitions["u2"][1] = "u2"
        self.state_transitions["u2"][2] = "u3"
        self.state_transitions["u2"][3] = "u2"
        self.state_transitions["u2"][4] = "u2"
        self.state_transitions["u2"][5] = "u5"
        self.state_transitions["u2"][6] = "u2"
        self.state_transitions["u2"][7] = "u2"

        self.state_transitions["u3"][0] = "u3"
        self.state_transitions["u3"][1] = "u3"
        self.state_transitions["u3"][2] = "u3"
        self.state_transitions["u3"][3] = "u4"
        self.state_transitions["u3"][4] = "u5"
        self.state_transitions["u3"][5] = "u3"
        self.state_transitions["u3"][6] = "u5"
        self.state_transitions["u3"][7] = "u3"

        self.state_transitions["u4"][0] = "u4"
        self.state_transitions["u4"][1] = "u4"
        self.state_transitions["u4"][2] = "u4"
        self.state_transitions["u4"][3] = "u4"
        self.state_transitions["u4"][4] = "u4"
        self.state_transitions["u4"][5] = "u4"
        self.state_transitions["u4"][6] = "u4"
        self.state_transitions["u4"][7] = "u5"

        self.state_transitions["u5"][0] = "u5"
        self.state_transitions["u5"][1] = "u5"
        self.state_transitions["u5"][2] = "u5"
        self.state_transitions["u5"][3] = "u5"
        self.state_transitions["u5"][4] = "u5"
        self.state_transitions["u5"][5] = "u5"
        self.state_transitions["u5"][6] = "u5"
        self.state_transitions["u5"][7] = "u5"

    def getLabel(self, state):
        # print(state)
        r0 = True
        r1 = False
        r2 = False
        g = False
        if self.isEnd(state):
            g = True

        if state[5] == 1:
            r0 = False
            r1 = True
            r2 = False
        elif state[5] == 2:
            r0 = False
            r1 = False
            r2 = True
        elif state[5] == 3:
            r0 = False
            r1 = False
            r2 = False
            
        return self.label[(r0, r1, r2, g)]

    def getSymbol(self, state, label):
        if label < 4:
            return self.symbols["empty"]
        if label == 4:
            return self.symbols["no_nse"]
        if label == 5 or label == 6:
            return self.symbols["mild"]
        return self.symbols["severe"]

    def symbolT(self, u, s, sym):
        symbol = self.getSymbol(u, self.getLabel(s))

        if sym == symbol:
            return 1
        return 0

    def T(self, u, s, u_):
        if (u, self.getLabel(s), u_) in self.transition_probabilities.keys():
            return self.transition_probabilities[(u, self.getLabel(s), u_)]

        sig = self.getLabel(s)
        next_u = self.state_transitions[u][sig]

        if next_u == u_:
            self.transition_probabilities[(u, s, u_)] = 1
            return 1
        else:
            self.transition_probabilities[(u, s, u_)] = 0
            return 0


if __name__ == '__main__':
    fsa = FSAConstants([((3, 6), (3, 6), True, 'p', 2)])
    trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'left'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'right'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((5, 3), (5, 4), False, 'p', 2), 'right'), (((5, 4), (5, 4), False, 'p', 2), 'pick_up'), (((5, 4), (5, 4), True, 'p', 2), 'up'), (((5, 5), (5, 5), True, 'p', 2), 'up'), (((4, 5), (4, 5), True, 'p', 2), 'up'), (((4, 6), (4, 6), True, 'p', 2), 'up'), (((3, 6), (3, 6), True, 'p', 2), 'drop'))
    # trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'down'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((4, 4), (5, 4), False, 'r', 3), 'down'), (((5, 4), (5, 4), False, 'p', 3), 'pick_up'), (((5, 4), (5, 4), True, 'p', 3), 'up'), (((4, 4), (4, 4), True, 'r', 4), 'up'), (((3, 4), (3, 4), True, 'r', 5), 'right'), (((3, 5), (3, 5), True, 'p', 5), 'right'), (((3, 6), (3, 6), True, 'p', 5), 'drop'), 'end')

    for i in trace:
        s = fsa.T("u3", i[0], "u5")
        print(i[0], fsa.getLabel(i[0]), s)
        print(fsa.getSymbol(fsa.getLabel(i[0])))