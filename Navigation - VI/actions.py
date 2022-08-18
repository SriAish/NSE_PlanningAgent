
class Actions:
    def __init__(self):
        self.left_slow = "ls"
        self.left_fast = "lf"
        self.right_slow = "rs"
        self.right_fast = "rf"
        self.up_slow = "us"
        self.up_fast = "uf"
        self.down_slow = "ds"
        self.down_fast = "df"

        self.fast_actions = [self.left_fast, self.right_fast, self.up_fast, self.down_fast]
        self.slow_actions = [self.left_slow, self.right_slow, self.up_slow, self.down_slow]
        self.all_actions = [self.left_slow, self.left_fast, self.right_slow, self.right_fast, self.up_slow, self.up_fast, self.down_slow, self.down_fast]

        self.fast_cost = 1
        self.slow_cost = 2

    def isFastAction(self, action):
        return action in self.fast_actions

    def isAction(self, action):
        return action in self.all_actions

    def isSlowAction(self, action):
        return action in self.slow_actions

    def getActionCost(self, action):
        if self.isFastAction(action):
            return self.fast_cost
        if self.isSlowAction(action):
            return self.slow_cost

    def isUp(self, action):
        if action == self.up_fast or action == self.up_slow:
            return True
        return False

    def isDown(self, action):
        if action == self.down_fast or action == self.down_slow:
            return True
        return False

    def isRight(self, action):
        if action == self.right_fast or action == self.right_slow:
            return True
        return False

    def isLeft(self, action):
        if action == self.left_fast or action == self.left_slow:
            return True
        return False

    def getSpeed(self, action):
        if self.isFastAction(action):
            return 'fast'
        if self.isSlowAction(action):
            return 'slow'

if __name__ == '__main__':
    action = Actions()
    print(action.isAction("df"), action.getActionCost("wrap"), action.getActionCost("pick_up"))