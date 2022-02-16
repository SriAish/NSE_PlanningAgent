class Actions:
    def __init__(self):
        self.down = "down"
        self.up = "up"
        self.right = "right"
        self.left = "left"
        self.pick_up = "pick_up"
        self.wrap = "wrap"
        self.allActions = [self.down, self.up, self.right, self.left, self.pick_up, self.wrap]
        self.boxActions = [self.pick_up]
        self.moveActions = [self.down, self.up, self.right, self.left]

        self.moveActionCost = 1
        self.boxActionCost = 2
        self.wrapActionCost = 5

    def isAction(self, action):
        return action in self.allActions

    def isBoxAction(self, action):
        return action in self.boxActions

    def isMoveAction(self, action):
        return action in self.moveActions

    def isWrapAction(self, action):
        return action == self.wrap

    def actionCost(self, action):
        if not self.isAction(action):
            return 0
        if self.isBoxAction(action):
            return self.boxActionCost
        if self.isWrapAction(action):
            return self.wrapActionCost
        
        return self.moveActionCost

if __name__ == '__main__':
    action = Actions()
    print(action.isAction("df"), action.actionCost("right"), action.actionCost("drop"))