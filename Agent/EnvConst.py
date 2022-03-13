from actions import Actions 
import copy
import numpy as np
import sys

class BoxPushingConstants:
    def __init__(self, grid_size = 7, rug_width = 3, rug_height = 3, rug_start = (2, 2), end_state = [], init_box_loc=(3, 0)):
        # Making the grrid
        self.grid_size = grid_size
        self.grid = np.full([grid_size, grid_size], 'p')
        
        # Making the rug
        self.rug_width = rug_width
        self.rug_height = rug_height
        self.rug_start = rug_start
        self.putRug()

        # Fixing the end state, initial location of box and generating other states
        self.end_state = end_state
        self.init_box_loc = init_box_loc
        self.generateStates()

        # Sstting up the actions
        self.actions = Actions()

        # Different action probability
        self.prob = 0.1

        # Hash table to maintain transition probabilities 
        self.transition_probabilities = {}
    
    def putRug(self):
        for i in range(self.rug_height):
            for j in range(self.rug_width):
                self.grid[self.rug_start[0] + i, self.rug_start[1] + j] = 'r'

    def getType(self, location):
        return self.grid[location]

    def generateStates(self):
        # state = (agent_location, box_location, box_picked_up, agent_wrapped, number_of_times_stepped_on_rug)
        self.states = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.states.append(((i, j), self.init_box_loc, False, False, self.getType((i, j))))
                if (i, j) == self.init_box_loc:
                    self.states.append(((i, j), (i, j), False, True, self.getType((i, j))))
                self.states.append(((i, j), (i, j), True, False, self.getType((i, j))))
                self.states.append(((i, j), (i, j), True, True, self.getType((i, j))))

    def getValidActions(self, state):
        actions = copy.deepcopy(self.actions.move_actions)

        if self.isEndState(state):
            return actions

        if state[0] == state[1] and state[1] == self.init_box_loc:
            actions.append(self.actions.wrap)

        if state[0] == state[1]:
            if not state[2]:
                actions.append(self.actions.pick_up)

        return actions
  
    def isEndState(self, state):
        return state in self.end_state or state == self.end_state

    def getCost(self, state, action):
        if self.isEndState(state):
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
        if action == self.actions.down:
            agent_locations_prob.append((self.moveDown(state[0]), 1 - self.prob))
            if state[0][1] != self.grid_size - 1:
                agent_locations_prob.append((self.moveRight(state[0]), self.prob))
            else:
                agent_locations_prob.append((self.moveLeft(state[0]), self.prob))

        elif action == self.actions.up:
            agent_locations_prob.append((self.moveUp(state[0]), 1 - self.prob))
            if state[0][1] != self.grid_size - 1:
                agent_locations_prob.append((self.moveRight(state[0]), self.prob))
            else:
                agent_locations_prob.append((self.moveLeft(state[0]), self.prob))

        elif action == self.actions.left:
            agent_locations_prob.append((self.moveLeft(state[0]), 1 - self.prob))
            if state[0][0] != self.grid_size - 1:
                agent_locations_prob.append((self.moveDown(state[0]), self.prob))
            else:
                agent_locations_prob.append((self.moveUp(state[0]), self.prob))

        elif action == self.actions.right:
            agent_locations_prob.append((self.moveRight(state[0]), 1 - self.prob))
            if state[0][0] != self.grid_size - 1:
                agent_locations_prob.append((self.moveDown(state[0]), self.prob))
            else:
                agent_locations_prob.append((self.moveUp(state[0]), self.prob))

        states = []

        for i in agent_locations_prob:
            if state[2]:
                box_location = i[0]
            else:
                box_location = state[1]
            states.append(((i[0], box_location, state[2], state[3], self.getType(i[0])), i[1]))

        return states, self.getCost(state, action)

    def wrap(self, state, action):
        return [((state[0], state[1], state[2], True, state[4]), 1)], self.getCost(state, action)

    def pick_up(self, state, action):
        if state[0] == state[1]:
            return [((state[0], state[1], True, state[3], state[4]), 1)], self.getCost(state, action)

        return [(state, 1)], self.getCost(state, action)

    def drop(self, state, action):
        if state[0] == state[1]:
            return [((state[0], state[1], False, state[3], state[4]), 1)], self.getCost(state, action)

    def transition(self, state, action):
        if self.isEndState(state):
            return [(state, 1)], self.getCost(state, action)

        if self.actions.isMoveAction(action):
            return self.move(state, action)

        if self.actions.isWrapAction(action):
            return self.wrap(state, action)

        if self.actions.isBoxAction(action):
            if action == self.actions.pick_up:
                return self.pick_up(state, action)
            if action == self.actions.drop:
                return self.drop(state, action)

    def T(self, s, a, s_):
        if (s, a, s_) in self.transition_probabilities.keys():
            return self.transition_probabilities[(s, a, s_)]
        trans, _ = self.transition(s, a)
        for i in trans:
            if s_ == i[0]:
                self.transition_probabilities[(s, a, s_)] = i[1]
                return i[1]

        self.transition_probabilities[(s, a, s_)] = 0
        
        return 0

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = [(g_pos, g_pos, True, False, 'p'), (g_pos, g_pos, True, True, 'p')]
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    
    s = ((1, 1), (1, 1), True, False, 'r')
    s_ = ((1, 2), (1, 2), True, False, 'p') 
    print(BP.T(s, "down", s_))