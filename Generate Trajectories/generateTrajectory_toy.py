from os import stat
from random import random
from Env import BPEnv
import copy
import numpy as np
import pickle
from actions import Actions
import random
from FSAConst import FSAConstants
A = Actions()
import sys

FSA = FSAConstants()

def checkDamage(t, st=[6, 4]):
    n = 0
    ind = 0
    for a, s in t:
        if A.isMoveAction(a) and s[2] and (not s[3]) and s[4] == 'r':
            ind += 1

    return (ind/9)*100

def generate_trajectory(agent, end_loc = (3, 6), box_loc = (3, 3)):
    env = BPEnv(1, 4, 1, 1, (0, 2), end_loc, box_loc)
    done = False

    t = []
    rug_c = 0
    ac = 0
    s = env.state()
    a = "No Action"
    t += [FSA.getLabel(s, a)]
    while not done and ac < 1000:
        if A.isMoveAction(a) and env.picked and env.onRug() and not env.wrapped:
            rug_c += 1

        a = agent.getAction(s)

        # t += [copy.deepcopy(s), a]

        ac += 1
        s, _, done = env.transition(a)
        # print(s, a)
        t += [FSA.getLabel(s, a)]

    # t += [copy.deepcopy(s)]

    return rug_c, t

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

def generate_mean_std(n, agent, new, end_loc, box_loc):
    if new: 
        nse = set()
        no_nse = set()
    else:
        nse = set(load("n_1_4_8"))
        no_nse = set(load("nn_1_4_8"))
    print(len(nse), len(no_nse))
    i = 0
    while i < n:
        i += 1
        rug_c, t = generate_trajectory(agent, end_loc, box_loc)
        if len(t) > 8:
            i -= 1
            continue
        if rug_c < 1:
            t += ['N']
            no_nse.add(tuple(t))
            # print("No Nse")
        else:
            t += ['S']
            # print("severe")
            nse.add(tuple(t))
    print(nse)
    print(no_nse)
    print(len(nse), len(no_nse))
    save("n_1_4_8", list(nse))
    save("nn_1_4_8", list(no_nse))

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
                self.prob1[s].append(policy[s][a])
                self.prob2[s].append(round(policy[s][a], 5))

    def getAction(self, state):
        x = random.random()
        try:
            if x < 0.95:
                return np.random.choice(self.pi[state], p = self.prob2[state])
            else:
                return np.random.choice(self.pi[state])
        except:
            # print(state, np.sum(self.prob2[state]))
            return np.random.choice(self.pi[state], p = self.prob1[state])

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    pol = "policy/VIp_1_4_" + sys.argv[5] + ".pkl"
    agent = Agent(pol)
    print(pol)
    generate_mean_std(10000, agent, False, (int(sys.argv[1]), int(sys.argv[2])), (int(sys.argv[3]), int(sys.argv[4])))
    # generate_trajectory(agent)