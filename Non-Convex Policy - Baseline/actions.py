class Actions:
    def __init__(self):
        self.down = "down"
        self.up = "up"
        self.right = "right"
        self.left = "left"
        self.pick_up = "pick_up"
        self.wrap = "wrap"
        self.drop = "drop"
        self.allActions = [self.down, self.up, self.right, self.left, self.pick_up, self.drop, self.wrap]
        self.boxActions = [self.pick_up, self.drop]
        self.wrapActions = [self.wrap]
        self.moveActions = [self.down, self.up, self.right, self.left]

        self.moveActionCost = 1
        self.boxActionCost = 2
        self.wrapCost = 5

    def isAction(self, action):
        return action in self.allActions

    def isBoxAction(self, action):
        return action in self.boxActions

    def isWrapAction(self, action):
        return action in self.wrapActions

    def actionCost(self, action):
        if not self.isAction(action):
            return 0
        if self.isBoxAction(action):
            return self.boxActionCost
        if self.isWrapAction(action):
            return self.wrapCost
        
        return self.moveActionCost

if __name__ == '__main__':
    action = Actions()
    print(action.isAction("df"), action.actionCost("right"), action.actionCost("drop"))