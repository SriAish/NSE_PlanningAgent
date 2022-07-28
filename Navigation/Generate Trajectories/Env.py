from actions import Actions 
import copy
import numpy as np
import sys
import random


class NavEnv:
    def __init__(self, grid_size = 7, pedestrian = [], puddle = [], init_loc = (0, 0), end_loc = (14, 14)):
        # Making the grrid
        self.grid_size = grid_size
        self.grid = np.full([grid_size, grid_size], 'r')
        
        # Making the rug
        self.pedestrian = pedestrian
        self.putPedestrian()
        self.puddle = puddle
        self.putPuddle()

        # Fixing the end state, initial location of box and generating other states
        self.generateStates()
        self.init_loc = init_loc
        self.end_location = end_loc

        # Sstting up the actions
        self.actions = Actions()

        # Different action probability
        self.prob = 0.1

        # state variables
        self.agent_location = self.init_loc
        self.speed = 'slow'
        self.ped = self.isPedestrian(self.agent_location)
        self.pud = self.isPuddle(self.agent_location)
        self.done = False

    def putPedestrian(self):
        for i in self.pedestrian:
            self.grid[i[0], i[1]] = 'H'
    
    def putPuddle(self):
        for i in self.puddle:
            self.grid[i[0], i[1]] = '@'

    def getType(self, location):
        return self.grid[location]

    def isPuddle(self, location):
        if self.getType(location) != 'r':
            return True
        return False

    def isPedestrian(self, location):
        if self.getType(location) == 'H':
            return True
        return False

    def state(self):
        return (self.agent_location, self.speed, self.ped, self.pud)

    def isEndState(self, state):
        return state in self.end_state or state == self.end_state

    def getValidActions(self):
        actions = copy.deepcopy(self.actions.all_actions)
        return actions

    def checkEnd(self):
        if self.agent_location == self.end_location:
            self.done = True
        return self.done

    def getCost(self, action):
        if self.done:
            return 0
        return self.actions.getActionCost(action)

    def moveDown(self, location):
        return (min(self.grid_size - 1, location[0] + 1), location[1])

    def moveUp(self, location):
        return (max(0, location[0] - 1), location[1])

    def moveLeft(self, location):
        return (location[0], max(0, location[1] - 1))

    def moveRight(self, location):
        return (location[0], min(self.grid_size - 1, location[1] + 1))

    def move(self, state, action):
        agent_locations_prob = []
        if self.actions.isDown(action):
            agent_locations_prob.append((self.moveDown(state[0]), 1 - self.prob))
            agent_locations_prob.append((self.moveRight(state[0]), self.prob))

        elif self.actions.isUp(action):
            agent_locations_prob.append((self.moveUp(state[0]), 1 - self.prob))
            agent_locations_prob.append((self.moveRight(state[0]), self.prob))

        elif self.actions.isLeft(action):
            agent_locations_prob.append((self.moveLeft(state[0]), 1 - self.prob))
            agent_locations_prob.append((self.moveDown(state[0]), self.prob))

        elif self.actions.isRight(action):
            agent_locations_prob.append((self.moveRight(state[0]), 1 - self.prob))
            agent_locations_prob.append((self.moveDown(state[0]), self.prob))

        states = []

        for i in agent_locations_prob:
            if self.getType((i[0][0], i[0][1])) == 'H':
                states.append(((i[0], self.actions.getSpeed(action), True, True), i[1]))
            if self.getType((i[0][0], i[0][1])) == '@':
                states.append(((i[0], self.actions.getSpeed(action), False, True), i[1]))
            else:
                states.append(((i[0], self.actions.getSpeed(action), False, False), i[1]))

        return states, self.getCost(state, action)

    def transition(self, state, action):
        if self.checkEnd(state):
            self.agent_location = (-1, -1)
            self.speed = 'slow'
            self.ped = False
            self.pud = False
            return [(state, 1)], self.getCost(state, action)

        return self.move(state, action)

