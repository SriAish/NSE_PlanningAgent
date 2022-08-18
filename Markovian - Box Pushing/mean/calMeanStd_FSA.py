from Env import BPEnv
from makeFSA import FSAConstants
import copy
import numpy as np
import pickle
import sys
from misc import load

def generate_trajectory(agent):
    env = BPEnv(15, 15, 7, 3, (6, 4), (7, 14), (7, 0))
    file_name = sys.argv[1][sys.argv[1].index("/")+1:]
    delta = load("results/delta/new_" + file_name + "_" + sys.argv[2] + "_best")
    omega = load("results/omega/new_" + file_name + "_" + sys.argv[2] + "_best")
    fsa = FSAConstants(delta, omega)
    done = False

    rug_c = 0
    ac = 0
    s = env.state()
    a = "No action"
    u = "0"
    u, sym = fsa.transition(u, a, s)
    nse = "N"
    count = 0
    while not done and ac < 100:
        if env.picked and env.onRug() and not env.wrapped:
            rug_c += 1
        # print(u, s)
        a = agent.getAction((u, s))
        # print(u, s, a)
        if s[2] and not s[3] and s[4] == 'r':
            count += 1
            if count < 6:
                nse = 'M'
            else:
                nse = 'S'
        ac += 1
        s, _, done = env.transition(a)
        u, sym = fsa.transition(u, a, s)
    # print(u, s, sym)
    # print(ac)
    if count > 0:
        return 'S'

    return 'N'

def generate_mean_std(n, agent):
    severe = []
    mild = []
    i = 0
    while i < n:
        i += 1
        sym = generate_trajectory(agent)
        if sym == 'N':
            severe.append(0)
            mild.append(0)
        elif sym == 'M':
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
            # print(state, np.sum(self.prob1[state]))
            return np.random.choice(self.pi[state], p = self.prob2[state])

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    pol = "policy/FSA_LP_p1_15_15_Mark_202.pkl"
    agent = Agent(pol)
    # print(pol)
    generate_mean_std(10000, agent)
    # generate_trajectory(agent)