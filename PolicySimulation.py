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
                self.prob[s].append(policy[s][a])
                # self.prob[s].append(round(policy[s][a], 7))

    def getAction(self, state):
        # print(np.sum(self.prob[state]))
        return np.random.choice(self.pi[state], p = self.prob[state])
        

def wrap_state(s):
    return (tuple(s[0]), tuple(s[1]), s[2], s[3])

def generate_trajectory(agent):
    env = env = BoxPushing(3, [0, 0], [2, 2], rug_width=0, rug_height=0, rug_start=[1, 1], locations=[[1,1]])
    done = False
    ac = 0
    su = 0
    gamma = 1
    while not done and ac < 1000:
        s = env.getState()
        a = agent.getAction(wrap_state(s))
        # print(ac, s)
        # env.display()
        s, c, done = env.getNextState(a)
        su += gamma*c
        gamma = gamma*0.9
        ac+=1
        # print(s, a, done)        
    # env.display()
    return su

def avg_n_trajectories(n, agent):
    severe = []
    mild = []
    s = 0    
    for i in range(n):
        s += generate_trajectory(agent)
    return s/n

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    agent = Agent(sys.argv[1])
    print("--------------------")
    print(sys.argv[1])
    print(avg_n_trajectories(1000, agent))
    print("--------------------")
    # generate_trajectory(agent)