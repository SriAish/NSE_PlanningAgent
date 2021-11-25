import pickle
import math
from actions import Actions

class Policy:
    def __init__(self, name, name2, name3, name4):
        self.loadPolicy(name)
        self.loadX(name2)
        file_to_read = open(name3, "rb")
        self.s1 = pickle.load(file_to_read)
        file_to_read = open(name4, "rb")
        self.s2 = pickle.load(file_to_read)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        self.policy = pickle.load(file_to_read)

    def loadX(self, name):
        file_to_read = open(name, "rb")
        self.x = pickle.load(file_to_read)

    def getAction(self, state):
        return self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])]

    def getPi(self):
        for key in self.policy:
            s = 0
            for a in self.policy[key]:
                s += math.e**self.policy[key][a]
            # print(s)
        for key in self.x:
            if math.e**self.x[key] < 0:
                print(math.e**self.x[key])
            if self.s1[key] < 0:
                print("s1: ",self.s1[key])
            if self.s2[key] < 0:
                print("s2: ",self.s2[key])
            # print(math.e**self.x[key])
            # print("s1: ",self.s1[key])
            # print("s2: ",self.s2[key])
            # if s < 0.9:
                # print(key)
                # print(self.policy[key])
                # print(s)

if __name__ == '__main__':
    agent = Policy('policy/Planning_Agent_Policy_3_3_9.pkl', 'policy/Planning_Agent_x_3_3_9.pkl', 'policy/Planning_Agent_s1_3_3_9.pkl', 'policy/Planning_Agent_s2_3_3_9.pkl')
    a = Actions()
    agent.getPi()
    # ((0, 0), (0, 0), False, 'p'), a.down
    # print(agent.policy)