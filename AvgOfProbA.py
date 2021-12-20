from misc import BoxPushingConstants
import sys
import pickle

class VIAgent:
    def __init__(self, BP, name, gamma = 0.9, delta = 0.001):
        self.BP = BP
        self.end_state = self.BP.end_state
        self.stateValues = {}
        self.initializeStateValues()
        self.gamma = gamma  
        self.delta = delta
        self.pi = self.loadPolicy(name)
        self.locations = [(int(int(self.BP.grid_size)/2), 1)]
        self.init_belief()

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

    def init_belief(self):
        if self.locations == None:
            self.locations = [(1, 1)]
        init_loc = (0, 0)
        self.belief_state = []
        for i in self.locations:
            self.belief_state.append((init_loc, i, False, 'p'))
    
    def initializeStateValues(self):
        for i in self.BP.states:
            self.stateValues[i] = sys.maxsize
        self.stateValues[self.end_state] = 0

    def avgProb(self):
        print(self.pi)
        nS = 0
        avg = 0
        for state in self.stateValues:
            if state == self.end_state:
                continue
            nS += 1
            for a in self.pi[state]:
                avg += self.pi[state][a]
        return avg/nS

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    # agent = VIAgent(BP, 'Dual LP - Gekko/policy/NC_Agent_Policy_3_3_max.pkl')
    agent = VIAgent(BP, 'Non-Convex Policy/policy/NC_Agent_Policy_nn_3_3_3.pkl')
    # agent = VIAgent(BP, 'Non-Convex Policy e_version/policy/NC_Agent_Policy_ni_3_3_3.pkl')
    # agent = VIAgent(BP, 'Convex Policy e_version/policy/C_Agent_Policy_ni_1_3_3.pkl')
    # agent = VIAgent(BP, 'Dual LP - Gekko/policy/NC_Agent_Policy_no_upper_3_31.pkl')
    # agent = VIAgent(BP, 'Dual LP/policy/DLP_Agent_Policy_3_3.pkl')
    # agent = VIAgent(BP, 'VI/policy_values/VIp_3_3.pkl')
    print(agent.avgProb())
