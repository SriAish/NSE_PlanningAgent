import numpy as np
import sys
import cvxpy as cp
from misc import BoxPushingConstants
import random


class PlanningAgent:
    def __init__(self, VIb = 6.4, gamma = 0.9, delta = 10, a1 = 1, a2 = 1):
        self.BP = BoxPushingConstants(3, 0, 0)
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.delta = delta
        self.a1 = a1
        self.a2 = a2
        self.VIb = VIb
        self.init_belief()
        print("initial belief setup")
        sys.stdout.flush()
        self.init_var()
        print("variables setup")
        sys.stdout.flush()
        self.init_para()
        print("parameters setup")
        sys.stdout.flush()
        self.get_event_traj()
        print("event trajectories setup")
        sys.stdout.flush()
        self.make_prob()
        print("problem setup")
        sys.stdout.flush()

    def init_belief(self):
        # locations = [(7, 0), (9, 2), (12, 7), (2, 7), (7, 12), (3, 11), (12, 14), (6, 3), (5, 6), (9, 8)]
        locations = [(1, 1)]
        init_loc = (0, 0)
        self.belief_state = []
        for i in locations:
            self.belief_state.append((init_loc, i, False, 'p'))

    def init_var(self):
        self.x = {}
        self.pi = {}
        for i in self.BP.states:
            self.x[i] = cp.Variable()
            actions = self.BP.getValidActions(i)
            self.pi[i] = {}
            for j in actions:
                self.pi[i][j] = cp.Variable()

    def init_para(self):
        self.x_para = {}
        self.pi_para = {}
        for i in self.BP.states:
            self.x_para[i] = random.uniform(0, 1)
            actions = self.BP.getValidActions(i)
            self.pi_para[i] = {}
            for j in actions:
                self.pi_para[i][j] = random.uniform(0, 1)
    
    def get_event_traj(self):
        self.mild = []
        self.severe = []

    def set_obj(self):
        print("starting to make objective")
        sys.stdout.flush()
        obj = 0
        for i in self.BP.states:
            for j in self.pi[i]:
                obj += cp.exp(self.x[i] + self.pi[i][j])*self.BP.get_cost(i, j)

        self.obj = cp.Minimize(obj)
        obj -= self.VIb 
        obj -= self.delta
        self.constraints = [obj <= 0]

    def make_constraints_eqn1(self):
        for s_ in self.BP.states:
            sys.stdout.flush()
            c = 0
            for s in self.BP.states:
                for a in self.pi[s]:
                    c += (cp.exp(self.x[s] + self.pi[s][a])*self.BP.T(s, a, s_))
            c = self.gamma*c
            if s_ in self.belief_state:
                c += 1/len(self.belief_state)
            c -= (cp.exp(self.x_para[s_])*(1 + self.x[s_] - self.x_para[s_]))
            self.constraints.append(c <= 0)

    def make_constraints_eqn2(self):
        for s_ in self.BP.states:
            c = 0
            for s in self.BP.states:
                for a in self.pi[s]:
                    c += (cp.exp(self.x_para[s] + self.pi_para[s][a])*self.BP.T(s, a, s_)*(1 + self.x[s] + self.pi[s][a] - self.x_para[s] - self.pi_para[s][a]))
            c = -self.gamma*c
            if s_ in self.belief_state:
                c -= 1/len(self.belief_state)
            c += cp.exp(self.x_para[s_])
            self.constraints.append(c <= 0) 

    def make_constraints_eqn3(self):
        pass

    def make_prob(self):
        self.constraints = []
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        sys.stdout.flush()
        self.make_constraints_eqn2()
        print("eq2")
        sys.stdout.flush()
        self.make_constraints_eqn3()
        print("eq3")
        sys.stdout.flush()
        self.prob = cp.Problem(self.obj, self.constraints)

    def solve_prob(self):
        try:
            self.prob.solve()
        except Exception as e:
            print(e)

    def solve_DCP(self):
        pass

    def print_policy(self):
        for i in self.pi:
            print(i)
            for j in self.pi[i]:
                print(j, self.pi[i][j].value)

if __name__ == '__main__':
    agent = PlanningAgent()
    agent.solve_prob()
    agent.print_policy()
    





