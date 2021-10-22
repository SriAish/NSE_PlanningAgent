class Actions:
    def __init__(self):
        self.south = "south"
        self.north = "north"
        self.east = "east"
        self.west = "west"
        self.pick_up = "pick_up"
        self.drop = "drop"
        self.allActions = [self.south, self.north, self.east, self.west, self.pick_up, self.drop]
        self.boxActions = [self.pick_up, self.drop]

        self.moveActionCost = 1
        self.boxActionCost = 2

    def isAction(self, action):
        return action in self.allActions

    def isBoxAction(self, action):
        return action in self.boxActions

    def actionCost(self, action):
        if not self.isAction(action):
            return 0
        if self.isBoxAction(action):
            return self.boxActionCost
        
        return self.moveActionCost

if __name__ == '__main__':
    action = Actions()
    print(action.isAction("df"), action.actionCost("east"), action.actionCost("drop"))