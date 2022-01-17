from numpy.random import gamma
from boxPushingEnv import BoxPushing
import sys
import numpy as np
import pickle

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
                # self.prob[s].append(policy[s][a])
                self.prob[s].append(round(policy[s][a], 5))

    def getAction(self, state):
        # print(np.sum(self.prob[state]))
        return np.random.choice(self.pi[state], p = self.prob[state])
        

def wrap_state(s):
    return (tuple(s[0]), tuple(s[1]), s[2], s[3])

def generate_trajectory(agent):
    env = env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[3, 0], [1, 2], [0, 3], [6, 3], [5, 4]])
    done = False
    ac = 0
    su = 0
    gamma = 1
    k = 0
    while not done and ac < 1000:
        s = env.getState()
        if s[3] == 'r':
                k += 1
        a = agent.getAction(wrap_state(s))
        # print(ac, s)
        # env.display()
        s, c, done = env.getNextState(a)
        su += gamma*c
        gamma = gamma*0.9
        ac+=1
        # print(s, a, done)        
    # env.display()
    return su, k

def avg_n_trajectories(n, agent):
    s = 0    
    co = 0
    for i in range(n):
        si, c = generate_trajectory(agent)
        s += si
        co += c
    return s/n, co

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    agent = Agent(sys.argv[1])
    print("--------------------")
    print(sys.argv[1])
    print(avg_n_trajectories(1000, agent))
    print("--------------------")
    # generate_trajectory(agent)