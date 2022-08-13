from Env import NavEnv
from makeFSA import FSAConstants
import copy
import numpy as np
import pickle
import sys
from misc import load

def save(name, t):
    file_to_write = open(name, "wb")
    pickle.dump(t, file_to_write)

def generate_trajectory(agent):
    ped = [(0, 12),(0, 13),(0, 14), (4, 0),(4, 1),(4, 5),(4, 6),(4, 7),(4, 8),(5, 9),(5, 10),(7, 0),(7, 1),(7, 10),(7, 11),(10, 0),(10, 1),(10, 2),(10, 3),(10, 9),(10, 10),(10, 11),(10, 12),(10, 13),(10, 14),(11, 0),(11, 1),(11, 2),(11, 3),(11, 5),(11, 6),(11, 7),(11, 8),(11, 9),(11, 10),(11, 11),(11, 12),(11, 13),(11, 14)]
    pud = [(0, 3),(0, 4),(0, 5),(0, 6),(4, 2),(4, 3),(4, 4),(4, 9),(5, 0),(5, 1),(5, 2),(7, 2),(7, 7),(7, 8),(7, 9),(11, 4)]
    env = NavEnv(15, ped, pud)
    file_name = sys.argv[1][sys.argv[1].index("/")+1:]
    delta = load("results/delta/new_ch_" + file_name + "_" + sys.argv[2] + "_0")
    omega = load("results/omega/new_ch_" + file_name + "_" + sys.argv[2] + "_0")
    fsa = FSAConstants(delta, omega)
    done = False

    ac = 0
    s = env.state()
    a = "No action"
    u = "0"
    u, sym = fsa.transition(u, a, s)
    nse = "N"
    pud_count = 0
    t = []
    t += [fsa.getLabel(s, a)]
    while not done and ac < 1000:
        # print(u, s)
        a = agent.getAction((u, s))
        # print(u, s, a)
        if env.ped and env.speed == 'fast':
            nse = 'S'
        elif nse != 'S' and env.pud and env.speed == 'fast':
            pud_count += 1
        ac += 1
        s, _, done = env.transition(a)
        u, sym = fsa.transition(u, a, s)
        t += [fsa.getLabel(s, a)]
    # print(u, s, sym)
    # print(ac)
    if pud_count/ac > 0.25 and nse == 'N':
        nse = 'M'
    return t, nse

def generate_mean_std(n, agent, new):
    if new: 
        severe = set()
        mild = set()
        no_nse = set()
    else:
        severe = set(load("nav_s_3"))
        mild = set(load("nav_m_3"))
        no_nse = set(load("nav_n_3"))
    print(len(severe), len(mild), len(no_nse))
    i = 0
    while i < n:
        i += 1
        t, sym = generate_trajectory(agent)
        if len(t) > 30:
            i -= 1
            continue
        t += [sym]
        if sym == 'N':
             no_nse.add(tuple(t))
        elif sym == 'M':
            mild.add(tuple(t))
        else:
            severe.add(tuple(t))

    print(t)
    print(len(no_nse), len(severe), len(mild))
    save("nav_s_4", list(severe))
    save("nav_m_4", list(mild))
    save("nav_n_4", list(no_nse))

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
    pol = "policy/FSA_LP_p_Nav_pol_300_2_5_15_1_1.pkl"
    agent = Agent(pol)
    # print(pol)
    generate_mean_std(10000, agent, True)
    # generate_trajectory(agent)