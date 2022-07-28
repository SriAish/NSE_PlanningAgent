# LABELS
# 0 : b, r, -g
# 1 : b, -r, -g
# 3 : b, -r, g
from actions import Actions 

class FSAConstants:
    def __init__(self):
        # Defining labels 
        self.label = {}
        self.label[(False, False, False)] = 0
        self.label[(False, True, False)] = 1
        self.label[(True, True, False)] = 2
        self.label[(False, False, True)] = 3

    def isEnd(self, state):
        return state[0] == (-1, -1)

    def getLabel(self, state, action):
        if self.isEnd(state):
            return self.label[(False, False, True)]
        fast = True
        if state[1] == 'slow':
            fast = False

        return self.label[(state[2] and fast, state[3] and fast, False)]