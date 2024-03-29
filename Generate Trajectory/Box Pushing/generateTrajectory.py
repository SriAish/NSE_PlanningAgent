from os import stat
from random import random
from Env import BPEnv
import copy
import numpy as np
import pickle
from actions import Actions
import random

A = Actions()

def checkDamage(t, st=[6, 4]):
    n = 0
    ind = 0
    for a, s in t:
        if A.isMoveAction(a) and s[2] and (not s[3]) and s[4] == 'r':
            ind += 1

    return (ind/9)*100

def generate_trajectory(agent, box_loc = (3, 3)):
    env = BPEnv(7, 3, 3, (2, 2), (3, 6), box_loc)
    done = False

    t = []
    rug_c = 0
    ac = 0
    s = env.state()
    a = "No Action"

    while not done and ac < 1000:
        if A.isMoveAction(a) and env.picked and env.onRug() and not env.wrapped:
            rug_c += 1

        a = agent.getAction(s)

        t += [copy.deepcopy(s), a]

        ac += 1
        s, _, done = env.transition(a)

    t += [copy.deepcopy(s)]

    return rug_c, t

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

def generate_mean_std(n, agent, new, box_loc):
    if new: 
        severe = set()
        mild = set()
        no_nse = set()
    else:
        severe = load("severe_trajectories")
        mild = load("mild_trajectories")
        no_nse = load("no_nse_trajectories")
    print(len(severe), len(mild), len(no_nse))
    i = 0
    while i < n:
        i += 1
        rug_c, t = generate_trajectory(agent, box_loc)
        if rug_c < 1:
            t += ["N"]
            no_nse.add(tuple(t))
            # print("No Nse")
        elif rug_c < 3:
            t += ["M"]
            # print("mild")
            mild.add(tuple(t))
        else:
            t += ["S"]
            # print("severe")
            severe.add(tuple(t))
    print(t)
    print(len(severe), len(mild), len(no_nse))
    save("severe_trajectories", severe)
    save("mild_trajectories", mild)
    save("no_nse_trajectories", no_nse)

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
            if x < 0.85:
                return np.random.choice(self.pi[state], p = self.prob2[state])
            else:
                return np.random.choice(self.pi[state])
        except:
            # print(state, np.sum(self.prob2[state]))
            return np.random.choice(self.pi[state], p = self.prob1[state])

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    pol = "policy/FSA_p3_7_7_10_4_2.pkl"
    agent = Agent(pol)
    print(pol)
    generate_mean_std(500, agent, False, (4, 2))
    # generate_trajectory(agent)