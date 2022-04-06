from Env import BPEnv
import copy
import numpy as np
import pickle

def generate_trajectory(agent):
    env = BPEnv(7, 3, 3, (2, 2), (3, 6), (3, 0))
    done = False

    rug_c = 0
    ac = 0

    while not done and ac < 1000:
        s = env.state()
        if env.picked and env.onRug() and not env.wrapped:
            rug_c += 1

        a = agent.getAction(s)

        ac += 1
        s, _, done = env.getNextState(a)

    return rug_c

def generate_mean_std(n, agent):
    severe = []
    mild = []
    i = 0
    while i < n:
        rug_c = generate_trajectory(agent)
        if rug_c < 1:
            severe.append(0)
            mild.append(0)
        elif rug_c < 3:
            severe.append(0)
            mild.append(1)
        else:
            severe.append(1)
            mild.append(0)

    print(len(severe), len(mild))
    print("severe : ", np.mean(severe), np.std(severe))
    print("milde : ", np.mean(mild), np.std(mild))

class Agent:
    def __init__(self, name):
        self.loadPolicy(name)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        policy = pickle.load(file_to_read)
        self.pi = {}
        self.prob = {}
        # print(policy)
        for s in policy:
            self.pi[s] = []
            self.prob[s] = []
            for a in policy[s]:
                self.pi[s].append(a)
                self.prob[s].append(policy[s][a])
                # self.prob[s].append(round(policy[s][a], 5))

    def getAction(self, state):
        state = (tuple(state[0]), tuple(state[1]), state[2], state[3])
        # if(np.sum(self.prob[state]) > 1):
        #     re = np.sum(self.prob[state]) - 1
        #     r = np.where(self.prob[state] == np.amax(self.prob[state]))
        #     # print(r[0])
        #     self.prob[state][r[0][0]] -= re
        return np.random.choice(self.pi[state], p = self.prob[state])

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    agent = Agent("policy/NC_Agent_Policy_nor_3_7_7_NSE_30_3.pkl")
    generate_mean_std(100, agent)
    # generate_trajectory(agent)