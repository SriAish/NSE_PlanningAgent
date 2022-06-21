from misc import BoxPushingConstants
import sys
import pickle

class VIAgent:
    def __init__(self, BP, gamma = 0.999, delta = 0.1):
        self.BP = BP
        g_pos = (int(sys.argv[6]), int(sys.argv[7]))
        e_state = []
        e_state.append(((-1, -1), (-1, -1), False, False, 'r'))
        self.end_state = e_state
        g_pos = (int(sys.argv[6]), int(sys.argv[7]))
        e_state = []
        e_state.append((g_pos, g_pos, True, False, 'p'))
        e_state.append((g_pos, g_pos, True, True, 'p'))
        self.check = e_state
        self.stateValues = {}
        self.initializeStateValues()
        self.gamma = gamma  
        self.delta = delta
        self.locations = [(int(sys.argv[10]), int(sys.argv[11]))]
        self.init_belief()

    def init_belief(self):
        init_loc = (0, 0)
        self.belief_state = []
        for i in self.locations:
            self.belief_state.append((init_loc, i, False, False, 'p'))
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
            # print(state, a, cost)
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
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = []
    e_state.append((g_pos, g_pos, True, False, 'p'))
    e_state.append((g_pos, g_pos, True, True, 'p'))
    print(e_state)
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state, (int(sys.argv[10]), int(sys.argv[11])))
    agent = VIAgent(BP, delta=0.001)
    policy = agent.generatePolicy()
    # print(policy)
    with open('policy_values/'+ sys.argv[8] + sys.argv[10] + sys.argv[11] + '.pkl', 'wb') as f:
        pickle.dump(policy, f)
    print("done")
    # # print(agent.stateValues)
    # with open('policy_values/'+ sys.argv[9] + '.pkl', 'wb') as f:
    #     pickle.dump(agent.stateValues, f, pickle.HIGHEST_PROTOCOL)
