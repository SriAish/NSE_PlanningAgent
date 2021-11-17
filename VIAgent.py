from misc import BoxPushingConstants
import pickle

class VIAgent:
    def __init__(self, BP, gamma = 0.9, delta = 0.1):
        self.BP = BP
        self.end_state = self.BP.end_state
        self.stateValues = {}
        self.initializeStateValues()
        self.gamma = gamma  
        self.delta = delta

    def initializeStateValues(self):
        for i in self.BP.states:
            self.stateValues[i] = 999
        self.stateValues[self.end_state] = 0

    def update(self):
        delta = 0
        for state in self.stateValues:
            if state == self.end_state:
                continue
            actions = self.BP.getValidActions(state)
            cost = 999999
            for i in actions:
                next_states, c = self.BP.transition(state, i)
                for j in next_states:
                    c += self.gamma * j[1] * self.stateValues[j[0]]
                cost = min(cost, c)
            delta = max(delta, abs(self.stateValues[state] - cost))
            self.stateValues[state] = cost

        return delta

    def generatePolicy(self):
        x = 999999
        k = 0
        while x > self.delta:
            x = self.update()
            k += 1
        
        policy = {}
        for state in self.stateValues:
            if state == self.end_state:
                continue
            actions = self.BP.getValidActions(state)
            cost = 999999
            for i in actions:
                next_states, c = self.BP.transition(state, i)
                for j in next_states:
                    c += self.gamma * j[1] * self.stateValues[j[0]]
                if c < cost:
                    a = i
                cost = min(cost, c)
            policy[state] = a

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
    BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = VIAgent(BP, delta=0.1)
    policy = agent.generatePolicy()
    # print(policy)
    with open('policy/'+ 'VIPolicy_7_7' + '.pkl', 'wb') as f:
        pickle.dump(policy, f, pickle.HIGHEST_PROTOCOL)
    
    # print(agent.stateValues)
    with open('policy/'+ 'ValueFunction_7_7' + '.pkl', 'wb') as f:
        pickle.dump(agent.stateValues, f, pickle.HIGHEST_PROTOCOL)
