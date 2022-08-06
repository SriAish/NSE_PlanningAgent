from misc import NavigationConstants
import sys
import pickle

class VIAgent:
    def __init__(self, BP, gamma = 0.999, delta = 0.1):
        self.BP = BP
        g_pos = (3, 6)
        e_state = []
        e_state.append(((-1, -1), '?', False, False))
        self.end_state = e_state
        g_pos = (3, 6)
        e_state = []
        e_state.append((g_pos, 'fast', False, False))
        e_state.append((g_pos, 'slow', False, False))
        self.check = e_state
        self.stateValues = {}
        self.initializeStateValues()
        self.gamma = gamma  
        self.delta = delta
        self.init_belief()

    def init_belief(self):
        init_loc = (0, 0)
        self.belief_state = []
        self.belief_state.append((init_loc, 'slow', False, False))
        print("belief")
        print(self.belief_state)

    def initializeStateValues(self):
        for i in self.BP.states:
            self.stateValues[i] = sys.maxsize
        for e in self.end_state:
            self.stateValues[e] = 0

    def update(self):
        delta = 0
        for state in self.stateValues:
            if state in self.end_state:
                continue
            actions = self.BP.getValidActions(state)
            state_cost = sys.maxsize
            # if state in self.check:
                # print(state)
            for action in actions:
                next_states, state_action_cost = self.BP.transition(state, action)
                # if state in self.check:
                #     print(next_states)
                for ns_prob in next_states:
                    state_action_cost += self.gamma * ns_prob[1] * self.stateValues[ns_prob[0]]
                state_cost = min(state_cost, state_action_cost)
            delta = max(delta, abs(self.stateValues[state] - state_cost))
            self.stateValues[state] = state_cost

        return delta

    def generatePolicy(self):
        x = sys.maxsize
        while x > self.delta:
            # print(x) 
            x = self.update()
        
        policy = {}
        for state in self.stateValues:
            policy[state] = {}
            if state in self.end_state:
                policy[state] = []
                continue
            actions = self.BP.getValidActions(state)
            cost = sys.maxsize
            for i in actions:
                policy[state][i] = 0
                next_states, c = self.BP.transition(state, i)
                for j in next_states:
                    c += self.gamma * j[1] * self.stateValues[j[0]]
                if c < cost:
                    a = i
                cost = min(cost, c)
            self.stateValues[state] = cost
            print(state)
            print("cost:", a, round(cost, 3))
            policy[state][a] = 1
        print(self.stateValues[self.belief_state[0]])
        return policy

class VIPolicy:
    def __init__(self, name):
        self.loadPolicy(name)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        self.policy = pickle.load(file_to_read)

    def getAction(self, state):
        return self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])]

if __name__ == '__main__':
    ped = [(0, 12),(0, 13),(0, 14),(4, 0),(4, 1),(4, 5),(4, 6),(4, 7),(4, 8),(5, 9),(5, 10),(7, 0),(7, 1),(7, 10),(7, 11),(10, 0),(10, 1),(10, 2),(10, 3),(10, 9),(10, 10),(10, 11),(10, 12),(10, 13),(10, 14),(11, 0),(11, 1),(11, 2),(11, 3),(11, 5),(11, 6),(11, 7),(11, 8),(11, 9),(11, 10),(11, 11),(11, 12),(11, 13),(11, 14)]
    pud = [(0, 3),(0, 4),(0, 5),(0, 6),(4, 2),(4, 3),(4, 4),(4, 9),(5, 0),(5, 1),(5, 2),(7, 2),(7, 7),(7, 8),(7, 9),(11, 4)]
    # ped = [(0, 1)]
    # pud = [(1, 0)]
    # ped = []
    # pud = []
    g_pos = (int(sys.argv[2]), int(sys.argv[3]))
    e_state = []
    e_state.append((g_pos, 'fast', False, False))
    e_state.append((g_pos, 'slow', False, False))
    print(e_state)
    BP = NavigationConstants(int(sys.argv[1]), ped, pud, e_state)
    agent = VIAgent(BP, delta=0.001)
    policy = agent.generatePolicy()
    # print(policy)
    with open('policy/'+ sys.argv[2] + "_" + sys.argv[3] + '.pkl', 'wb') as f:
        pickle.dump(policy, f)
    print("done")
    # print(agent.stateValues)
    # with open('policy_values/'+ sys.argv[9] + '.pkl', 'wb') as f:
    #     pickle.dump(agent.stateValues, f, pickle.HIGHEST_PROTOCOL)
