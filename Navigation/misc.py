from actions import Actions 
import copy
import numpy as np
import sys

class NavigationConstants:
    def __init__(self, grid_size = 7, pedestrian = [], puddle = [],  goal_state = []):
        # Making the grrid
        self.grid_size = grid_size

        self.grid = np.full([self.grid_size, self.grid_size], 'r')
        
        # Making the rug
        self.pedestrian = pedestrian
        self.putPedestrian()
        self.puddle = puddle
        self.putPuddle()

        # Fixing the end state, initial location of box and generating other states
        print("goal: ", goal_state)
        self.goal_state = goal_state
        self.generateStates()

        # Sstting up the actions
        self.actions = Actions()

        # Different action probability
        self.prob = 0.1

        # Hash table to maintain transition probabilities 
        self.transition_probabilities = {}
    
    def putPedestrian(self):
        for i in self.pedestrian:
            self.grid[i[0], i[1]] = 'p'
    
    def putPuddle(self):
        for i in self.puddle:
            if self.grid[i[0], i[1]] == 'p':
                self.grid[i[0], i[1]] = '-'
            else:
                self.grid[i[0], i[1]] = '_'

    def getType(self, location):
        return self.grid[location]

    def generateStates(self):
        # state = (agent_location, box_location, box_picked_up, agent_wrapped, number_of_times_stepped_on_rug)
        self.states = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.getType((i, j)) == '-':
                    self.states.append(((i, j), 'fast', True, True))
                    self.states.append(((i, j), 'slow', True, True))
                if self.getType((i, j)) == 'p':
                    self.states.append(((i, j), 'fast', True, False))
                    self.states.append(((i, j), 'slow', True, False))
                if self.getType((i, j)) == '_':
                    self.states.append(((i, j), 'fast', False, True))
                    self.states.append(((i, j), 'slow', False, True))
                else:
                    self.states.append(((i, j), 'fast', False, False))
                    self.states.append(((i, j), 'slow', False, False))
        self.end_state = ((-1, -1), '?', False, False)
        self.states.append(self.end_state)

    def getValidActions(self, state):
        actions = copy.deepcopy(self.actions.all_actions)
        return actions
  
    def isGoalState(self, state):
        return state in self.goal_state or state == self.goal_state

    def isEndState(self, state):
        return state in self.end_state or state == self.end_state

    def getCost(self, state, action):
        if self.isGoalState(state) or self.isEndState(state):
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
            if self.getType((i[0][0], i[0][1])) == '-':
                states.append(((i[0], self.actions.getSpeed(action), True, True), i[1]))
            if self.getType((i[0][0], i[0][1])) == 'p':
                states.append(((i[0], self.actions.getSpeed(action), True, False), i[1]))
            if self.getType((i[0][0], i[0][1])) == '_':
                states.append(((i[0], self.actions.getSpeed(action), False, True), i[1]))
            else:
                states.append(((i[0], self.actions.getSpeed(action), False, False), i[1]))


        return states, self.getCost(state, action)

    def transition(self, state, action):
        if self.isEndState(state):
            return [(state, 1)], self.getCost(state, action)

        if self.isGoalState(state):
            return [(self.end_state, 1)], self.getCost(state, action)

        return self.move(state, action)

    def T(self, s, a, s_):
        if (s, a, s_) in self.transition_probabilities.keys():
            return self.transition_probabilities[(s, a, s_)]
        trans, _ = self.transition(s, a)
        self.transition_probabilities[(s, a, s_)] = 0
        for i in trans:
            if s_ == i[0]:
                self.transition_probabilities[(s, a, s_)] += i[1]
        
        return self.transition_probabilities[(s, a, s_)]

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = [(g_pos, g_pos, True, False, 'p'), (g_pos, g_pos, True, True, 'p')]
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    
    s = ((1, 1), (1, 1), True, False, 'r')
    s_ = ((1, 2), (1, 2), True, False, 'p') 
    print(BP.T(s, "down", s_))