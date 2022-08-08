from email import policy
from Env import BPEnv
import copy
import numpy as np
import pickle

def generate_trajectory(agent):
    env = BPEnv(15, 15, 7, 3, (6, 4), (7, 14), (7, 0))
    done = False

    rug_c = 0
    ac = 0

    while not done and ac < 100:
        s = env.state()
        if env.picked and env.onRug() and not env.wrapped:
            rug_c += 1

        a = agent.getAction(s)

        ac += 1
        s, _, done = env.transition(a)

    return rug_c

def generate_mean_std(n, agent):
    severe = []
    mild = []
    i = 0
    while i < n:
        i += 1
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
    print("mild : ", np.mean(mild), np.std(mild))

class Agent:
    def __init__(self, name):
        self.loadPolicy(name)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        policy = pickle.load(file_to_read)
        self.pi = {}
        self.prob1 = {}
        self.prob2 = {}
        # print(policy)
        for s in policy:
            self.pi[s] = []
            self.prob1[s] = []
            self.prob2[s] = []
            for a in policy[s]:
                self.pi[s].append(a)
                self.prob2[s].append(policy[s][a])
                self.prob1[s].append(round(policy[s][a], 5))

    def getAction(self, state):
        # if(np.sum(self.prob[state]) > 1):
        #     re = np.sum(self.prob[state]) - 1
        #     r = np.where(self.prob[state] == np.amax(self.prob[state]))
        #     # print(r[0])
        #     self.prob[state][r[0][0]] -= re
        try:
            return np.random.choice(self.pi[state], p = self.prob1[state])
        except:
            print(state, np.sum(self.prob1[state]))
            return np.random.choice(self.pi[state], p = self.prob2[state])

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    pol = "Sandhya_learned_pol_15_15_opt_20.pkl"
    agent = Agent(pol)
    print(pol)
    generate_mean_std(10000, agent)
    # generate_trajectory(agent)