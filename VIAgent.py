
import numpy as np
import pickle
from actions import Actions

class BoxPushingConstants:
    def __init__(self, grid_size = 15):
        self.grid_size = grid_size
        self.grid = np.full([grid_size, grid_size], 'p')

        self.putRug()
        self.generateStates()

        self.actions = Actions()
    
    def putRug(self):
        rug_height = 3
        rug_width = 7
        rug_start = (6, 4)
        for i in range(rug_height):
            for j in range(rug_width):
                self.grid[rug_start[0] + i, rug_start[1] + j] = 'r'

    def getType(self, location):
        return self.grid[tuple(location)]

    def getValidActions(self, state):
        actions = self.actions.moveActions
        if state[0] == state[1]:
            if state[2]:
                actions.append(self.actions.drop)
            else:
                actions.append(self.actions.pick_up)

        return actions

    def generateStates(self):
        self.states = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                for k in range(self.grid_size):
                    for l in range(self.grid_size):
                        self.states.append(((i, j), (k, l), False, self.getType([i, j])))
                        if [i, j] == [k, l]:
                            self.states.append(((i, j), (k, l), True, self.getType([i, j])))

    def moveDown(self, location):
        return (min(self.grid_size - 1, location[0] + 1), location[1])

    def moveUp(self, location):
        return (max(0, location[0] - 1), location[1])

    def moveLeft(self, location):
        return (location[0], max(0, location[1] - 1))

    def moveRight(self, location):
        return (location[0], min(self.grid_size - 1, location[1] + 1))

    def transition(self, state, action):
        if self.actions.isBoxAction(action):
            if state[0] != state[1]:
                return [(state, 1)], self.actions.actionCost(action)
            if action == self.actions.pick_up:
                return [((state[0], state[1], True, state[3]), 1)], self.actions.actionCost(action)
            else:
                return [((state[0], state[1], False, state[3]), 1)], self.actions.actionCost(action)
        else:
            agent_locations_prob = []
            if action == self.actions.down:
                agent_locations_prob.append((self.moveDown(state[0]), 0.9))
                if state[0][1] != self.grid_size - 1:
                    agent_locations_prob.append((self.moveRight(state[0]), 0.1))
                else:
                    agent_locations_prob.append((self.moveLeft(state[0]), 0.1))

            elif action == self.actions.up:
                agent_locations_prob.append((self.moveUp(state[0]), 0.9))
                if state[0][1] != self.grid_size - 1:
                    agent_locations_prob.append((self.moveRight(state[0]), 0.1))
                else:
                    agent_locations_prob.append((self.moveLeft(state[0]), 0.1))

            elif action == self.actions.left:
                agent_locations_prob.append((self.moveLeft(state[0]), 0.9))
                if state[0][0] != self.grid_size - 1:
                    agent_locations_prob.append((self.moveDown(state[0]), 0.1))
                else:
                    agent_locations_prob.append((self.moveUp(state[0]), 0.1))

            elif action == self.actions.right:
                agent_locations_prob.append((self.moveRight(state[0]), 0.9))
                if state[0][0] != self.grid_size - 1:
                    agent_locations_prob.append((self.moveDown(state[0]), 0.1))
                else:
                    agent_locations_prob.append((self.moveUp(state[0]), 0.1))

            states = []

            for i in agent_locations_prob:
                if state[2]:
                    box_location = i[0]
                else:
                    box_location = state[1]
                states.append(((i[0], box_location, state[2], self.getType(i[0])), i[1]))

            return states, self.actions.actionCost(action)

class VIAgent:
    def __init__(self, endState, gamma = 0.9, delta = 0.1):
        self.BP = BoxPushingConstants()
        self.endState = endState
        self.stateValues = {}
        self.initializeStateValues()
        self.gamma = gamma  
        self.delta = delta

    def initializeStateValues(self):
        for i in self.BP.states:
            self.stateValues[i] = 999
        self.stateValues[self.endState] = 0

    def update(self):
        delta = 0
        for state in self.stateValues:
            if state == self.endState:
                continue
            actions = self.BP.getValidActions(state)
            cost = 999999
            for i in actions:
                next_states, c = self.BP.transition(state, i)
                for j in next_states:
                    c += self.gamma * j[1] * self.stateValues[j[0]]
                cost = min(cost, c)
            delta = max(delta, abs(self.stateValues[state] - cost))
            self.stateValues[state] = cost

        return delta

    def generatePolicy(self):
        x = 999999
        k = 0
        print(len(self.stateValues))
        while x > self.delta:
            x = self.update()
            k += 1
            print(k, x)
        
        policy = {}
        for state in self.stateValues:
            if state == self.endState:
                continue
            actions = self.BP.getValidActions(state)
            cost = 999999
            for i in actions:
                next_states, c = self.BP.transition(state, i)
                for j in next_states:
                    c += self.gamma * j[1] * self.stateValues[j[0]]
                if c < cost:
                    a = i
                cost = min(cost, c)
            policy[state] = a

        return policy

if __name__ == '__main__':
    agent = VIAgent(((7, 14), (7, 14), False, 'p'))
    policy = agent.generatePolicy()
    print(policy)
    with open('policy/'+ 'VIPolicy' + '.pkl', 'wb') as f:
        pickle.dump(policy, f, pickle.HIGHEST_PROTOCOL)