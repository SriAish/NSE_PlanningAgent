from random import random
from Env import NavEnv
import copy
import numpy as np
import pickle
from actions import Actions
import random
from FSAConstants import FSAConstants
A = Actions()
import sys

FSA = FSAConstants()
# ped = [(0, 12),(0, 13),(0, 14),(4, 0),(4, 1),(4, 5),(4, 6),(4, 7),(4, 8),(5, 9),(5, 10),(7, 0),(7, 1),(7, 10),(7, 11),(10, 0),(10, 1),(10, 2),(10, 3),(10, 9),(10, 10),(10, 11),(10, 12),(10, 13),(10, 14),(11, 0),(11, 1),(11, 2),(11, 3),(11, 5),(11, 6),(11, 7),(11, 8),(11, 9),(11, 10),(11, 11),(11, 12),(11, 13),(11, 14)] + [(0, 3),(0, 4),(0, 5),(0, 6),(4, 2),(4, 3),(4, 4),(4, 9),(5, 0),(5, 1),(5, 2),(7, 2),(7, 7),(7, 8),(7, 9),(11, 4)]
ped = []
pud = [(0, 3),(0, 4),(0, 5),(0, 6),(4, 2),(4, 3),(4, 4),(4, 9),(5, 0),(5, 1),(5, 2),(7, 2),(7, 7),(7, 8),(7, 9),(11, 4)] + [(0, 12),(0, 13),(0, 14),(4, 0),(4, 1),(4, 5),(4, 6),(4, 7),(4, 8),(5, 9),(5, 10),(7, 0),(7, 1),(7, 10),(7, 11),(10, 0),(10, 1),(10, 2),(10, 3),(10, 9),(10, 10),(10, 11),(10, 12),(10, 13),(10, 14),(11, 0),(11, 1),(11, 2),(11, 3),(11, 5),(11, 6),(11, 7),(11, 8),(11, 9),(11, 10),(11, 11),(11, 12),(11, 13),(11, 14)]

def checkDamage(t, st=[6, 4]):
    n = 0
    ind = 0
    # for a, s in t:
    #     if A.isMoveAction(a) and s[2] and (not s[3]) and s[4] == 'r':
    #         ind += 1

    return (ind/9)*100

def generate_trajectory(agent, end_loc = (3, 6), init_loc = (3, 3)):
    env = NavEnv(15, ped, pud, init_loc, end_loc)
    done = False

    t = []
    sp = False
    pud_cnt = 0
    ac = 0
    s = env.state()
    a = "No Action"
    t += [FSA.getLabel(s, a)]
    while not done and ac < 400:
        # print(s)
        ac+=1
        if s[1] == 'fast' and s[3]:
            pud_cnt += 1
        if s[3] and s[2] and s[1] == 'fast':
            sp = True

        a = agent.getAction(s)

        # t += [copy.deepcopy(s), a]

        s, _, done = env.transition(s, a)
        # print(s, a)
        t += [FSA.getLabel(s, a)]

    # t += [copy.deepcopy(s)]

    return ac, pud_cnt, sp, t

def load(name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

def generate_mean_std(n, agent, new, end_loc, box_loc):
    if new: 
        severe = set()
        mild = set()
        no_nse = set()
    else:
        severe = set(load("nav_15_15_s"))
        mild = set(load("nav_15_15_m"))
        no_nse = set(load("nav_15_15_nn"))
    print(len(severe), len(mild), len(no_nse))
    i = 0
    while i < n:
        i += 1
        path, pud_cnt, sp, t = generate_trajectory(agent, end_loc, box_loc)
        if len(t) > 25:
            i -= 1
            continue
        if sp:
            t += ['S']
            severe.add(tuple(t))
            # print("No Nse")
        elif pud_cnt/path > 0.25:
            t += ['M']
            # print("mild")
            mild.add(tuple(t))
        else:
            t += ['N']
            no_nse.add(tuple(t))
            # print("severe")
            
    print(t)
    print(len(severe), len(mild), len(no_nse))
    # print(severe)
    save("nav_15_15_s", list(severe))
    save("nav_15_15_m", list(mild))
    save("nav_15_15_nn", list(no_nse))

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
            # print(self.pi)
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
    pol = "policy/3_5only_pud" + ".pkl"
    agent = Agent(pol)
    print(pol)
    generate_mean_std(10000, agent, False, (int(sys.argv[1]), int(sys.argv[2])), (int(sys.argv[3]), int(sys.argv[4])))
    # generate_trajectory(agent)