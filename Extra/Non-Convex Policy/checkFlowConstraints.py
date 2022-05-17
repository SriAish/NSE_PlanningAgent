import pickle
import math
import sys
from misc import BoxPushingConstants
# from actions import Actions

class FlowConstraint:
    def __init__(self, BP, x_name, pi_name, grid_size, gamma = 0.9):
        self.x = self.loadPolicy(x_name)
        self.pi = self.loadPolicy(pi_name)
        self.gamma = gamma
        self.BP = BP
        self.locations = [(3, 0), (1, 2), (0, 3), (6, 3), (5, 4)]
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
        for s_ in self.x:
            # LHS
            lhs = 0
            for a in self.pi[s_]:
                lhs += self.x[s_]*self.pi[s_][a]

            # RHS
            rhs = 0
            for s in self.x:
                for a in self.pi[s]:
                    rhs += self.BP.T(s, a, s_)*self.x[s]*self.pi[s][a]

            rhs = self.gamma*rhs

            if s_ in self.belief_state:
                rhs += 1/len(self.belief_state)

            if abs(lhs - rhs) < 0.00001:
                cf += 1
            else:
                icf += 1
                print(lhs, rhs)

        print(cf, icf)
            

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    agent = FlowConstraint(BP, 'policy/NC_Agent_x_nor_3_7_7_NSE4.pkl', 'policy/NC_Agent_Policy_nor_3_7_7_NSE4.pkl', sys.argv[1])
    # a = Actions()
    agent.checkFlow()
    # print(agent.getPi(((0, 0), (0, 0), False, 'p'), a.down))
    # print(agent.policy)