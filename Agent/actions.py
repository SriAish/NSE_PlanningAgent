
class Actions:
    def __init__(self):
        self.up = "up"
        self.down = "down"
        self.left = "left"
        self.right = "right"
        self.pick_up = "pick_up"
        self.drop = "drop"
        self.wrap = "wrap"

        self.move_actions = [self.down, self.up, self.right, self.left]
        self.all_actions = [self.down, self.up, self.right, self.left, self.pick_up, self.wrap]
        self.box_actions = [self.pick_up]

        self.move_cost = 1
        self.box_action_cost = 1
        self.wrap_cost = 5

    def isMoveAction(self, action):
        return action in self.move_actions

    def isAction(self, action):
        return action in self.all_actions

    def isBoxAction(self, action):
        return action in self.box_actions

    def isWrapAction(self, action):
        return action == self.wrap

    def getActionCost(self, action):
        if self.isMoveAction(action):
            return self.move_cost
        if self.isBoxAction(action):
            return self.box_action_cost
        if self.isWrapAction(action):
            return self.wrap_cost

if __name__ == '__main__':
    action = Actions()
    print(action.isAction("df"), action.getActionCost("wrap"), action.getActionCost("pick_up"))