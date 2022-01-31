from boxPushingEnv import BoxPushing
import csv
import copy
import numpy as np
import pickle

def checkDamage(t, st=[6, 4]):
    rug = np.zeros((3, 3))
    n = 0
    ind = 0
    for i, _ in t:
        # print("string: ", i)
        if type(i) is str:
            continue
        if i[3] == 'r':
            rug[i[0][0] - st[0], i[0][1] - st[1]] = 1
        ind += 1
    
    # print(rug)
    
    # print(np.count_nonzero(rug))

    return (np.count_nonzero(rug)/9) * 100

def wrap_state(s):
    return (tuple(s[0]), tuple(s[1]), s[2], s[3])

def generate_trajectory(agent):
    env = env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[0, 0], [0, 1], [0, 5], [0, 6], [1, 0], [1, 1], [1, 5], [1, 6], [5, 0], [5, 1], [5, 5], [5, 6], [6, 0], [6, 1], [6, 5], [6, 6]])
    # env = env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[3, 0], [1, 2], [0, 3], [6, 3], [5, 4]])
    done = False
    t = []
    ac = 0
    while not done and ac < 1000:
        s = env.getState()
        a = agent.getAction(s)
        # print(ac, s)
        # env.display()
    
        t = t + [(wrap_state(copy.deepcopy(s)), a)]

        ac += 1
        s, _, done = env.getNextState(a)

        # print(s, a, done)        
    # env.display()
    return t, ac

def generate_n_tajectories(n, agent):
    severe = []
    locations = [(3, 0), (1, 2), (0, 3), (6, 3), (5, 4)]
    env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[3, 0], [1, 2], [0, 3], [6, 3], [5, 4]])
    up = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 5), (3, 1), (3, 5), (4, 1), (4, 5), (5, 2), (5, 3), (5, 4)]
    for _ in range(5):
        for i in up:
            for j in locations:
                t = []
                s = (i, j, False, 'p')
                a = agent.getAction(s)
                t = t + [(s, a)]
                env.setState(s)
                s, _, done = env.getNextState(a)
                a = agent.getAction(s)
                t = t + [(wrap_state(copy.deepcopy(s)), a)]
                if s[3] == 'r':
                    severe.append(t)
            s = (i, i, True, 'p')
            a = agent.getAction(s)
            t = t + [(s, a)]
            env.setState(s)
            s, _, done = env.getNextState(a)
            a = agent.getAction(s)
            t = t + [(wrap_state(copy.deepcopy(s)), a)]
            if s[3] == 'r':
                severe.append(t)
    print(len(severe))
    file_to_write = open("severe_trajectories", "wb")
    pickle.dump(severe, file_to_write)

class VIPolicy:
    def __init__(self, name):
        self.loadPolicy(name)

    def loadPolicy(self, name):
        file_to_read = open(name, "rb")
        self.policy = pickle.load(file_to_read)

    def getAction(self, state):
        action = 'down'
        pr = 0
        # print(state)
        for key in self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])]:
            if pr < self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])][key]:
                pr = self.policy[(tuple(state[0]), tuple(state[1]), state[2], state[3])][key]
                action = key
        return action

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
        # print(np.sum(self.prob[state]))
        
        # if(np.sum(self.prob[state]) < 1):
            # print(np.sum(self.prob[state]))
            # self.prob[state][0] += 1 - np.sum(self.prob[state])
        if(np.sum(self.prob[state]) > 1):
            re = np.sum(self.prob[state]) - 1
            r = np.where(self.prob[state] == np.amax(self.prob[state]))
            # print(r[0])
            self.prob[state][r[0][0]] -= re
        return np.random.choice(self.pi[state], p = self.prob[state])

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    agent = Agent("policy_values/NC_Agent_Policy_nor_3_7_7_4.pkl")
    generate_n_tajectories(1000, agent)
    # generate_trajectory(agent)