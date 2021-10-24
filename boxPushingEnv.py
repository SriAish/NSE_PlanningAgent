import numpy as np
import random
import copy
import os
import time
from actions import Actions
np.set_printoptions(infstr="(infinity)")

class BoxPushing:
    def __init__(self, grid_size=None, initial_location=None, end_location=None, box_location=None, rug_width=None, rug_height=None, rug_start=None):
        if grid_size == None:
            grid_size = 15
        self.grid_size = grid_size
        self.grid = np.full([grid_size, grid_size], 'p')

        self.putRug(rug_width, rug_height, rug_start)

        if initial_location == None:
            initial_location = [0, 0]
        self.agent_location = initial_location

        self.end_location = None
        if end_location == None:
            end_location = self.randomEmptyCell()
        self.end_location = end_location

        if box_location == None:
            box_location = self.randomEmptyCell()
        self.box_location = box_location

        self.box_pushing = False

        self.finishCost = 10

        self.actions = Actions()
        self.totalCost = 0
        self.done = False

    def checkDone(self):
        if self.agent_location == self. box_location and self.box_location == self.end_location and not self.box_pushing:
            self.done = True
        return self.done

    def putRug(self, rug_width, rug_height, rug_start):
        if rug_width == None or rug_height == None:
            rug_height = 3
            rug_width = 7
            rug_start = (6, 4)
        for i in range(rug_height):
            for j in range(rug_width):
                self.grid[rug_start[0] + i, rug_start[1] + j] = 'r'

    def getValidActions(self):
        actions = self.actions.moveActions
        if self.agent_location == self.box_location:
            if self.box_pushing:
                actions = actions + [self.actions.drop]
            else:
                actions = actions + [self.actions.pick_up]

        return actions

    def randomEmptyCell(self):
        location = None

        while location == None or location == self.agent_location or location == self.end_location:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            location = [x, y]

        return location

    def moveSouth(self):
        self.agent_location[0] = min(self.grid_size - 1, self.agent_location[0] + 1)

    def moveNorth(self):
        self.agent_location[0] = max(0, self.agent_location[0] - 1)

    def moveWest(self):
        self.agent_location[1] = max(0, self.agent_location[1] - 1)

    def moveEast(self):
        self.agent_location[1] = min(self.grid_size - 1, self.agent_location[1] + 1)

    def move(self, action):
        if not self.actions.isAction(action):
            raise Exception("Not a valid action")

        prob = random.random()

        if self.actions.isBoxAction(action):
            if self.agent_location != self.box_location:
                return
            if action == self.actions.pick_up:
                self.box_pushing = True
            else:
                self.box_pushing = False
        else:
            if action == self.actions.south:
                if prob > 0.9:
                    self.moveEast()
                else:
                    self.moveSouth()
            elif action == self.actions.north:
                if prob > 0.9:
                    self.moveWest()
                else:
                    self.moveNorth()
            elif action == self.actions.west:
                if prob > 0.9:
                    self.moveNorth()
                else:
                    self.moveWest()
            elif action == self.actions.east:
                if prob > 0.9:
                    self.moveSouth()
                else:
                    self.moveEast()
            if self.box_pushing == True:
                self.box_location = self.agent_location

    def getType(self):
        return self.grid[tuple(self.agent_location)]

    def getState(self):
        return (self.agent_location, self.box_location, self.box_pushing, self.getType())

    def getNextState(self, action):
        self.move(action)
        cost = self.actions.actionCost(action)
        if self.checkDone():
            cost -= self.finishCost
        self.totalCost += cost
        s = self.getState()
        return s, cost, self.done

    def display(self):
        tempGrid = copy.deepcopy(self.grid)
        rows = self.grid.shape[0]
        cols = self.grid.shape[1]
        tempGrid[tuple(self.box_location)] = 'b'
        tempGrid[tuple(self.end_location)] = 'e'
        tempGrid[tuple(self.agent_location)] = 'a'
        _ = os.system('clear')
        print(np.matrix(tempGrid))  
        print("------------------------------------------")
        time.sleep(1)

if __name__ == '__main__':
    env = BoxPushing()
    print(env.getState())
    print(env.getNextState("east"))
    print(env.getValidActions())
    env.agent_location = env.end_location
    env.box_location = env.end_location
    print(env.getNextState("drop"))
    env.box_pushing = True
    print(env.getValidActions())
