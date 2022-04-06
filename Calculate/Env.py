from actions import Actions 
import copy
import numpy as np
import sys
import random


class BPEnv:
    def __init__(self, grid_size = 7, rug_width = 3, rug_height = 3, rug_start = (2, 2), end_location = (3, 6), init_box_loc=(3, 0)):
        # Making the grrid
        self.grid_size = grid_size
        self.grid = np.full([grid_size, grid_size], 'p')
        
        # Making the rug
        self.rug_width = rug_width
        self.rug_height = rug_height
        self.rug_start = rug_start
        self.putRug()

        # Fixing the end state, initial location of box and generating other states
        self.end_location = end_location
        self.init_box_loc = init_box_loc

        # Sstting up the actions
        self.actions = Actions()

        # Different action probability
        self.prob = 0.05

        # Hash table to maintain transition probabilities 
        self.agent_location = (0, 0)
        self.box_location = init_box_loc
        self.picked = False
        self.wrapped = False

    def state(self):
        return (self.agent_location, self.box_location, self.picked, self.wrapped, self.getType(self.agent_location))

    def getValidActions(self, state):
        actions = copy.deepcopy(self.actions.move_actions)

        if self.isGoalState(state) or self.isEndState(state):
            return actions

        if state[0] == state[1] and state[1] == self.init_box_loc and not state[3]:
            actions.append(self.actions.wrap)

        if state[0] == state[1]:
            if not state[2]:
                actions.append(self.actions.pick_up)

        return actions
        
    def putRug(self):
        for i in range(self.rug_height):
            for j in range(self.rug_width):
                self.grid[self.rug_start[0] + i, self.rug_start[1] + j] = 'r'

    def getType(self, location):
        return self.grid[location]

    def checkDone(self):
        if self.agent_location == self. box_location and self.box_location == self.end_location:
            self.done = True
        return self.done

    def getCost(self, action):
        if self.done:
            return 0
        return self.actions.getActionCost(action)

    def moveDown(self):
        self.agent_location[0] = min(self.grid_size - 1, self.agent_location[0] + 1)

    def moveUp(self):
        self.agent_location[0] = max(0, self.agent_location[0] - 1)

    def moveLeft(self):
        self.agent_location[1] = max(0, self.agent_location[1] - 1)

    def moveRight(self):
        self.agent_location[1] = min(self.grid_size - 1, self.agent_location[1] + 1)

    def move(self, action):
        prob = random.random()
        if action == self.actions.down:
            if prob < self.prob:
                self.moveRight()
            elif prob < 2*self.prob:
                self.moveLeft()
            else:
                self.moveDown()
        elif action == self.actions.up:
            if prob < self.prob:
                self.moveRight()
            elif prob < 2*self.prob:
                self.moveLeft()
            else:
                self.moveUp()
        elif action == self.actions.left:
            if prob < self.prob:
                self.moveDown()
            elif prob < 2*self.prob:
                self.moveUp()
            else:
                self.moveLeft()
        elif action == self.actions.right:
            if prob < self.prob:
                self.moveDown()
            elif prob < 2*self.prob:
                self.moveUp()
            else:
                self.moveRight()
        if self.picked == True:
            self.box_location = self.agent_location

    def wrap(self):
        self.wrapped = True

    def pick_up(self):
        self.pick_up = True

    def transition(self, action):
        a = self.getValidActions(self.state())

        if action not in a:
            print("Invalid Action")
            return "Invalid Action" 

        if self.done:
            self.state(), self.getCost(action)

        if self.actions.isMoveAction(action):
            self.move(action)

        if self.actions.isWrapAction(action):
            self.wrap()

        if self.actions.isBoxAction(action):
            if action == self.actions.pick_up:
                self.pick_up()

        self.checkDone()

        return self.state, self.getCost(action), self.done

