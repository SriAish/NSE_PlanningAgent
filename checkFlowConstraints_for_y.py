import pickle
import math
import sys
from misc import BoxPushingConstants
# from actions import Actions

class FlowConstraint:
    def __init__(self, BP, y_name, grid_size, gamma = 0.9):
        self.y = self.loadPolicy(y_name)
        self.gamma = gamma
        self.BP = BP
        self.locations = [(int(int(grid_size)/2), 1)]
        self.init_belief()
        
    def init_belief(self):
        if self.locations == None:
            self.locations = [(1, 1)]
        init_loc = (0, 0)
        self.belief_state = []
        for i in self.locations:
            self.belief_state.append((init_loc, i, False, 'p'))

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

    def getAction(self, state):
        return self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])]

    def checkFlow(self):
        cf = 0
        icf = 0
        for s_ in self.y:
            # LHS
            lhs = 0
            for a in self.y[s_]:
                lhs += self.y[s_][a]

            # RHS
            rhs = 0
            for s in self.y:
                for a in self.y[s]:
                    rhs += self.BP.T(s, a, s_)*self.y[s][a]

            rhs = self.gamma*rhs

            if s_ in self.belief_state:
                rhs += 1/len(self.belief_state)

            if abs(lhs - rhs) <= 0.00001:
                cf += 1
            else:
                icf += 1
                print(lhs, rhs)

        print(cf, icf)
            

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    agent = FlowConstraint(BP, 'Dual LP - Gekko/policy/NC_Agent_y_no_upper_3_31.pkl', sys.argv[1])
    # a = Actions()
    agent.checkFlow()
    # print(agent.getPi(((0, 0), (0, 0), False, 'p'), a.down))
    # print(agent.policy)