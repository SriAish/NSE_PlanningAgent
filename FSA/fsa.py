# LABELS
# 0 : b, r0, -r>0,<=25, -g
# 1 : b, -r0, r>0,<=25, -g
# 2 : b, -r0, -r>0,<=25, -g
# 3 : b, r0, -r>0,<=25, g
# 4 : b, -r0, r>0,<=25, g
# 5 : b, -r0, -r>0,<=25, g


class FSA:
    def __init__(self):
        self.states = {}
        self.states["u0"] = {}
        self.states["u1"] = {}
        self.states["u2"] = {}
        self.states["u3"] = {}
        self.states["u4"] = {}
        self.states["u5"] = {}

        self.stateTransition()

        self.label = {}
        self.label[(True, False, False)] = 0
        self.label[(False, True, False)] = 1
        self.label[(False, False, False)] = 2
        self.label[(True, False, True)] = 3
        self.label[(False, True, True)] = 4
        self.label[(False, False, True)] = 5

        self.state = "u0"
        self.r0 = True
        self.r25 = False
        self.g = False

    def stateTransition(self):
        self.states["u0"][0] = "u2"
        self.states["u0"][1] = "u1"
        self.states["u0"][2] = "u0"
        self.states["u0"][3] = "u5"
        self.states["u0"][4] = "u0"
        self.states["u0"][5] = "u0"

        self.states["u1"][0] = "u1"
        self.states["u1"][1] = "u1"
        self.states["u1"][2] = "u4"
        self.states["u1"][3] = "u1"
        self.states["u1"][4] = "u5"
        self.states["u1"][5] = "u1"

        self.states["u2"][0] = "u2"
        self.states["u2"][1] = "u3"
        self.states["u2"][2] = "u2"
        self.states["u2"][3] = "u5"
        self.states["u2"][4] = "u2"
        self.states["u2"][5] = "u2"

        self.states["u3"][0] = "u3"
        self.states["u3"][1] = "u3"
        self.states["u3"][2] = "u4"
        self.states["u3"][3] = "u3"
        self.states["u3"][4] = "u5"
        self.states["u3"][5] = "u3"

        self.states["u4"][0] = "u4"
        self.states["u4"][1] = "u4"
        self.states["u4"][2] = "u4"
        self.states["u4"][3] = "u4"
        self.states["u4"][4] = "u4"
        self.states["u4"][5] = "u5"

    def getLabel(self, obs):
        if obs == "end":
            self.g = True
            return self.label[(self.r0, self.r25, self.g)]

        obs = obs[0]
        if obs[4] > 0 and obs[4] < 3:
            self.r0 = False
            self.r25 = True
        elif obs[4] >= 3:
            self.r0 = False
            self.r25 = False
            
        return self.label[(self.r0, self.r25, self.g)]

    def getSymbol(self):
        if self.g == False:
            return "E"
        if self.r0 == True:
            return "N"
        if self.r25 == True:
            return "M"
        return "S"

    def getNextState(self, obs):
        if self.state == "u5":
            return

        l = self.getLabel(obs)

        self.state = self.states[self.state][l]

        return self.state

if __name__ == '__main__':
    fsa = FSA()
    trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'left'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'right'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((5, 3), (5, 4), False, 'p', 2), 'right'), (((5, 4), (5, 4), False, 'p', 2), 'pick_up'), (((5, 4), (5, 4), True, 'p', 2), 'up'), (((5, 5), (5, 5), True, 'p', 2), 'up'), (((4, 5), (4, 5), True, 'p', 2), 'up'), (((4, 6), (4, 6), True, 'p', 2), 'up'), (((3, 6), (3, 6), True, 'p', 2), 'drop'), 'end')
    # trace = ((((0, 0), (5, 4), False, 'p', 0), 'down'), (((1, 0), (5, 4), False, 'p', 0), 'down'), (((2, 0), (5, 4), False, 'p', 0), 'right'), (((2, 1), (5, 4), False, 'p', 0), 'down'), (((3, 1), (5, 4), False, 'p', 0), 'down'), (((4, 1), (5, 4), False, 'p', 0), 'right'), (((4, 2), (5, 4), False, 'r', 1), 'right'), (((4, 3), (5, 4), False, 'r', 2), 'down'), (((4, 4), (5, 4), False, 'r', 3), 'down'), (((5, 4), (5, 4), False, 'p', 3), 'pick_up'), (((5, 4), (5, 4), True, 'p', 3), 'up'), (((4, 4), (4, 4), True, 'r', 4), 'up'), (((3, 4), (3, 4), True, 'r', 5), 'right'), (((3, 5), (3, 5), True, 'p', 5), 'right'), (((3, 6), (3, 6), True, 'p', 5), 'drop'), 'end')
    s = fsa.state
    print(fsa.state)
    for i in trace:
        s = fsa.getNextState(i)
        print(fsa.state)
    print(fsa.getSymbol())
