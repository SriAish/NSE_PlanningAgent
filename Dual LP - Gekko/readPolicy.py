import pickle
import math
from actions import Actions

class Policy:
    def __init__(self, name):
        self.loadPolicy(name)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        self.policy = pickle.load(file_to_read)

    def getAction(self, state):
        return self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])]

    def getPi(self, state, action):
        for key in self.policy:
            s = 0
            for a in self.policy[key]:
                s += self.policy[key][a]
            if s != 1:
                # print(key)
                # print(self.policy[key])
                print(s)
        return self.policy[state][action]

if __name__ == '__main__':
    agent = Policy('policy/NC_Agent_Policy_3_3.pkl')
    a = Actions()
    print(agent.getPi(((0, 0), (0, 0), False, 'p'), a.down))
    # print(agent.policy)