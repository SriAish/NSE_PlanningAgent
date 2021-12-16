import pickle
import math
import sys
from misc import BoxPushingConstants
# from actions import Actions

class FlowConstraint:
    def __init__(self, BP, y_name, name2, name3, grid_size, gamma = 0.9):
        self.y = self.loadPolicy(y_name)
        self.state_to_index = self.loadPolicy(name2)
        self.action_to_index = self.loadPolicy(name3)
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
        for s_ in self.BP.states:
            # LHS
            actions = self.BP.getValidActions(s_)
            lhs = 0
            for a in actions:
                lhs += self.y[self.state_to_index[s_]+ self.action_to_index[a]]

            # RHS
            rhs = 0
            for s in self.BP.states:
                actions = self.BP.getValidActions(s)
                for a in actions:
                    rhs += self.BP.T(s, a, s_)*self.y[self.state_to_index[s]+ self.action_to_index[a]]

            rhs = self.gamma*rhs

            if s_ in self.belief_state:
                rhs += 1/len(self.belief_state)

            if abs(lhs - rhs) <= 0.0:
                cf += 1
            else:
                icf += 1
                print(lhs, rhs)

        print(cf, icf)
            

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    agent = FlowConstraint(BP, 'policy/DLP_Agent_SLSQP_Policy_3_3.pkl', 'policy/DLP_Agent_SLSQP_state_ind_3_3.pkl', 'policy/DLP_Agent_SLSQP_action_ind_3_3.pkl', sys.argv[1])
    # a = Actions()
    agent.checkFlow()
    # print(agent.getPi(((0, 0), (0, 0), False, 'p'), a.down))
    # print(agent.policy)