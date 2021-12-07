import numpy as np
import sys
import cvxpy as cp
from misc import BoxPushingConstants
import random
import pickle
import csv


class PlanningAgent:
    def __init__(self, BP, VIb = 6.4, gamma = 0.9, delta = 10, a1 = 1, a2 = 1, locations = None):
        self.BP = BP
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.delta = delta
        self.a1 = a1
        self.a2 = a2
        self.VIb = VIb
        self.s1 = cp.Variable(self.no_states)
        self.s2 = cp.Variable(self.no_states)
        self.tao = cp.Parameter()
        self.tao.value = 1
        self.mu = 1.5
        self.tao_max = 20
        self.locations = locations
        with open('mild_trajectories', 'rb') as f:
            self.mild = pickle.load(f)
        with open('severe_trajectories', 'rb') as f:
            self.severe = pickle.load(f)
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
        if self.locations == None:
            self.locations = [(1, 1)]
        init_loc = (0, 0)
        self.belief_state = []
        for i in self.locations:
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
            self.x_para[i] = cp.Parameter()
            self.x_para[i].value = random.uniform(-10, 0)
            actions = self.BP.getValidActions(i)
            self.pi_para[i] = {}
            for j in actions:
                self.pi_para[i][j] = cp.Parameter()
                self.pi_para[i][j].value = random.uniform(-10, 0)

    def change_para(self):
        for i in self.BP.states:
            self.x_para[i].value = self.x[i].value
            for j in self.pi[i]:
                self.pi_para[i][j].value = self.pi[i][j].value
    
    def get_event_traj(self):
        self.mild = []
        self.severe = []

    def set_obj(self):
        print("starting to make objective")
        print(self.BP.states)
        sys.stdout.flush()
        obj = 0
        for i in self.BP.states:
            print(i)
            for j in self.pi[i]:
                print(j)
                obj += cp.exp(self.x[i] + self.pi[i][j])*self.BP.get_cost(i, j)

        self.obj = cp.Minimize(obj + self.tao*(cp.sum(self.s1) + cp.sum(self.s2)))
        obj -= self.VIb 
        obj -= self.delta
        self.constraints = [obj <= 0]

    def make_constraints_eqn1(self):
        i = 0
        for s_ in self.BP.states:
            sys.stdout.flush()
            c = 0
            for s in self.BP.states:
                for a in self.pi[s]:
                    if self.BP.T(s, a, s_) != 0:
                        c += (cp.exp(self.x[s] + self.pi[s][a])*self.BP.T(s, a, s_))
            c = self.gamma*c
            if s_ in self.belief_state:
                c += 1/len(self.belief_state)
            c -= (cp.exp(self.x_para[s_])*(1 + self.x[s_] - self.x_para[s_]))
            self.constraints.append(c <= self.s1[i])
            i += 1

    def make_constraints_eqn2(self):
        i = 0
        for s_ in self.BP.states:
            c = 0
            for s in self.BP.states:
                for a in self.pi[s]:
                    if self.BP.T(s, a, s_) != 0:
                        c += (cp.exp(self.x_para[s] + self.pi_para[s][a])*self.BP.T(s, a, s_)*(1 + self.x[s] + self.pi[s][a] - self.x_para[s] - self.pi_para[s][a]))
            c = -self.gamma*c
            if s_ in self.belief_state:
                c -= 1/len(self.belief_state)
            c += cp.exp(self.x_para[s_])
            self.constraints.append(c <= self.s2[i])
            i += 1 

    def make_constraints_eqn3(self):
        for i in self.x:
            self.constraints.append(cp.exp(self.x[i]) <= 1)

        for i in self.pi:
            for j in self.pi[i]:
                self.constraints.append(cp.exp(self.pi[i][j]) <= 1)

    def make_constraints_eqn4(self):
        c = 0
        for i in self.severe:
            n = len(i)
            j = 0
            es = self.x[i[j]]
            j = 1
            m = 1
            while i < n:
                es = es + self.pi[i[j-1]][i[j]]
                m = m*self.BP.T(i[j-1], i[j], i[j+1])
                i += 2

            c = c + m*cp.exp(es)
            
        self.constraints.append(c <= self.a1)
                

        c = 0
        for i in self.mild:
            n = len(i)
            j = 0
            es = self.x[i[j]]
            j = 1
            m = 1
            while i < n:
                es = es + self.pi[i[j-1]][i[j]]
                m = m*self.BP.T(i[j-1], i[j], i[j+1])
                i += 2

            c = c + m*cp.exp(es)
            
        self.constraints.append(c <= self.a2)

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
        self.make_constraints_eqn4()
        print("eq4")
        sys.stdout.flush()
        self.prob = cp.Problem(self.obj, self.constraints)

    def solve_prob(self):
        try:
            self.prob.solve(solver=cp.SCS, verbose=True)
        except Exception as e:
            print(e)

    def solve_DCP(self):
        with open('output_7_7.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["iteration", "V", "para", "tao"])
            for i in range(10):
                self.tao.value = min(self.mu*self.tao.value, self.tao_max)
                self.solve_prob()
                csvwriter.writerow([i, self.prob.value, self.x_para[self.belief_state[0]].value, self.tao.value])
                self.change_para()

    def print_policy(self):
        policy = {}
        for i in self.pi:
            print(i)
            max_ac = None
            max_val = 0
            for j in self.pi[i]:
                v = np.exp(self.pi[i][j].value)
                print(j, v)
                if v > max_val :
                    max_val = v
                    max_ac = j
            policy[i] = max_ac
        print(policy)
        with open('policy/'+ 'Planning_Agent_Policy_7_7_DCP' + '.pkl', 'wb') as f:
            pickle.dump(policy, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = PlanningAgent(BP)
    agent.solve_DCP()
    agent.print_policy()
    




