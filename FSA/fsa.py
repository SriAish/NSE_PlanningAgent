# LABELS
# 0 : b, r0, -r>0,<=25, -g
# 1 : b, -r0, r>0,<=25, -g
# 2 : b, -r0, -r>0,<=25, -g
# 3 : b, r0, -r>0,<=25, -g
# 4 : b, -r0, r>0,<=25, -g
# 5 : b, -r0, -r>0,<=25, -g


class FSA:
    def __init__(self):
        states = {}
        states["u0"] = {}
        states["u1"] = {}
        states["u2"] = {}
        states["u3"] = {}
        states["u4"] = {}
        states["u5"] = {}

        label = {}
        label[(True, False, False)] = 0
        label[(False, True, False)] = 1
        label[(False, False, False)] = 2
        label[(True, False, True)] = 3
        label[(False, True, True)] = 4
        label[(False, False, True)] = 5

    def label(self, state):
        if state[5] 