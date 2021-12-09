import pickle
import math
# from actions import Actions

class Policy:
    def __init__(self, name, name2):
        self.policy = self.loadPolicy(name)
        self.policy2 = self.loadPolicy(name2)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

    def getAction(self, state):
        return self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])]

    def getPi(self):
        for key in self.policy:
            if self.policy[key] != self.policy2[key]:
                # print(key)
                # print(self.policy[key])
                print(key, self.policy[key], self.policy2[key])
        return

if __name__ == '__main__':
    agent = Policy('Dual LP/policy/DLP_Agent_Policy_3_3_max.pkl', 'VI/policy_values/VIp_3_3.pkl')
    # a = Actions()
    agent.getPi()
    # print(agent.getPi(((0, 0), (0, 0), False, 'p'), a.down))
    # print(agent.policy)