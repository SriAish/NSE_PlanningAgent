import pygame as pg
import numpy as np
from boxPushingEnv import BoxPushing
import pickle
import sys

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

colors = np.array([[120, 250, 90], [250, 90, 120], [255, 255, 255]])

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
        print(np.sum(self.prob[state]))
        print(state, self.pi[state], self.prob[state])
        return np.random.choice(self.pi[state], p = self.prob[state])
        

def wrap_state(s):
    return (tuple(s[0]), tuple(s[1]), s[2], s[3])

# agent2 = Agent('Non-Convex Policy/policy/NC_Agent_Policy_nor_3_7_7_5.pkl')
agent = Agent('Non-Convex Policy/policy/NC_Agent_Policy_nor_3_7_7_NSE_all.pkl')
env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[3, 0]])
# env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[3, 0], [1, 2], [0, 3], [6, 3], [5, 4]])
done = False
ac = 0
su = 0
gamma = 1
k = 0
while not done and ac < 1000:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    s = env.getState()
    gridarray = env.display()
    surface = pg.surfarray.make_surface(colors[gridarray])
    surface = pg.transform.scale(surface, (200, 200))  # Scaled a bit.
    if s[3] == 'r':
            k += 1
    a = agent.getAction(wrap_state(s))
    s, c, done = env.getNextState(a)
    ac+=1
    screen.fill((30, 30, 30))
    screen.blit(surface, (100, 100))
    pg.display.flip()
    clock.tick(1)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((30, 30, 30))
    screen.blit(surface, (100, 100))
    pg.display.flip()
    clock.tick(60)