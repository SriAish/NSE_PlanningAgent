import random
import numpy as np 

class RandomAgent:
    def __init__(self, endState):
        self.endState = endState
        print(self.endState)
        self.numberToActions = {
            1 : "north",
            2 : "south",
            3 : "east",
            4 : "west",
            5 : "pick_up",
            6 : "drop"
        }

    def getAction(self, state):
        actions = [1, 2, 3, 4]
        pr_a = [0, 0, 0, 0]
        if state[0] == state[1]:
            if self.endState == state[0]:
                return "drop"
            elif not state[2]:
                return "pick_up"
            else:
                if state[0][0] < self.endState[0]:
                    pr_a[1] = 0.4
                elif state[0][0] > self.endState[0]:
                    pr_a[0] = 0.4

                if state[0][1] < self.endState[1]:
                    pr_a[2] = 0.4
                elif state[0][1] > self.endState[1]:
                    pr_a[3] = 0.4
                
                if pr_a[1] == pr_a[0]:
                    if pr_a[2] == 0:
                        pr_a[3] += 0.3
                    else:
                        pr_a[2] += 0.3

                if pr_a[2] == pr_a[3]:
                    if pr_a[0] == 0:
                        pr_a[1] += 0.3
                    else:
                        pr_a[0] += 0.3

                for i in range(4):
                    if pr_a[i] == 0:
                        pr_a[i] = 0.1
                print(pr_a)
                return self.numberToActions[np.random.choice(actions, 1, p = pr_a)[0]]

        if state[0][0] < state[1][0]:
            pr_a[1] = 0.4
        elif state[0][0] > state[1][0]:
            pr_a[0] = 0.4

        if state[0][1] < state[1][1]:
            pr_a[2] = 0.4
        elif state[0][1] > state[1][1]:
            pr_a[3] = 0.4
        
        if pr_a[1] == pr_a[0]:
            if pr_a[2] == 0:
                pr_a[3] += 0.3
            else:
                pr_a[2] += 0.3

        if pr_a[2] == pr_a[3]:
            if pr_a[0] == 0:
                pr_a[1] += 0.3
            else:
                pr_a[0] += 0.3

        for i in range(4):
            if pr_a[i] == 0:
                pr_a[i] = 0.1
        # print(pr_a)
        return self.numberToActions[np.random.choice(actions, 1, p = pr_a)[0]]

if __name__ == '__main__':
    state = ([1, 1], [2,2], False, 'p')
    agent = RandomAgent([3,3])
    print(agent.getAction(state))