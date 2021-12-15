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

    def update(self):
        delta = 0
        for state in self.stateValues:
            if state == self.end_state:
                continue
            st_val = 0
            for a in self.pi[state]:
                # print(a, self.pi[state][a])
                # if(self.pi[state][a] < 0): 
                #     continue
                next_states, c = self.BP.transition(state, a)
                for j in next_states:
                    # c += self.gamma * j[1] * self.stateValues[j[0]]
                    c += self.gamma * j[1] * self.pi[state][a] * self.stateValues[j[0]]
                st_val += c
            # print(st_val)
            delta = max(delta, abs(self.stateValues[state] - st_val))
            self.stateValues[state] = st_val
        # print(delta)
        return delta

    def getSV(self):
        x = sys.maxsize
        k = 0
        while x > self.delta:
            x = self.update()
            k += 1
        # print(self.stateValues)
        return self.stateValues[self.belief_state[0]]

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    # agent = VIAgent(BP, 'Dual LP - Gekko/policy/NC_Agent_Policy_3_3_max.pkl')
    agent = VIAgent(BP, 'Dual LP - Gekko/policy/NC_Agent_Policy_3_3.pkl')
    # agent = VIAgent(BP, 'Dual LP/policy/DLP_Agent_Policy_3_3_max.pkl')
    # agent = VIAgent(BP, 'VI/policy_values/VIp_3_3.pkl')
    print(agent.getSV())
