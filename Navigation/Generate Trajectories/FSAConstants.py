# LABELS
# 0 : b, r, -g
# 1 : b, -r, -g
# 3 : b, -r, g
from actions import Actions 

class FSAConstants:
    def __init__(self):
        # Defining labels 
        self.label = {}
        self.label[(False, False, False, False)] = 0
        self.label[(True, False, False, False)] = 1
        self.label[(False, False, True, False)] = 2
        self.label[(True, False, True, False)] = 3
        self.label[(False, True, True, False)] = 4
        self.label[(True, True, True, False)] = 5
        self.label[(False, False, False, True)] = 6

    def isEnd(self, state):
        return state[0] == (-1, -1)

    def getLabel(self, state, action):
        if self.isEnd(state):
            return self.label[(False, False, False, True)]
        fast = True
        if state[1] == 'slow':
            fast = False

        return self.label[(fast, state[2], state[3], False)]