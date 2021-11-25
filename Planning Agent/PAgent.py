import sys
import cvxpy as cp
from misc import BoxPushingConstants
import random
import pickle
import csv

class PlanningAgent:
    def __init__(self, BP, gamma = 0.9, locations = None):
        self.BP = BP
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.locations = locations
        self.tao = cp.Parameter()
        self.tao.value = 1
        self.mu = 10
        self.tao_max = 100000
        self.init_belief()
        print("initial belief setup")
        sys.stdout.flush()
        self.init_var()
        print("variables setup")
        self.init_para()
        print("parameters setup")
        sys.stdout.flush()
        self.init_intermediates()
        self.make_prob()
        print("problem setup")
        sys.stdout.flush()
    
    def init_belief(self):
        if self.locations == None:
            self.locations = [(1, 1)]
        init_loc = (0, 0)
        self.belief_state = []
        for i in self.locations:
            self.belief_state.append((init_loc, i, False, 'p'))

    def init_var(self):
        self.x = {}
        self.pi = {}
        self.s1 = {}
        self.s2 = {}
        for s in self.BP.states:
            self.pi[s] = {}
            self.x[s] = cp.Variable()
            self.s1[s] = cp.Variable()
            self.s2[s] = cp.Variable()
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.pi[s][a] = cp.Variable()

    def init_para(self):
        self.x_para = {}
        self.pi_para = {}
        for s in self.BP.states:
            self.x_para[s] = cp.Parameter()
            self.x_para[s].value = random.uniform(-1, 0)
            actions = self.BP.getValidActions(s)
            self.pi_para[s] = {}
            for a in actions:
                self.pi_para[s][a] = cp.Parameter()
                self.pi_para[s][a].value = random.uniform(-1, 0)

    def change_para(self):
        for i in self.BP.states:
            self.x_para[i].value = self.x[i].value
            for j in self.pi[i]:
                self.pi_para[i][j].value = self.pi[i][j].value

    def init_intermediates(self):
        self.in_y = {}
        self.in_y_para = {}
        for s in self.BP.states:
            self.in_y[s] = {} 
            self.in_y_para[s] = {}
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.in_y[s][a] = cp.exp(self.x[s] + self.pi[s][a])
                self.in_y_para[s][a] = cp.exp(self.x_para[s] + self.pi_para[s][a])

    def set_obj(self):
        obj = 0
        slack = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                obj += self.in_y[s][a]*self.BP.get_cost(s, a)
            slack += self.s1[s] + self.s2[s]

        self.obj = cp.Minimize(obj + (self.tao*slack))

    def make_constraints_eqn1(self):
        for s_ in self.BP.states:
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)
            y = cp.exp(self.x_para[s_])*(1 + self.x[s_] - self.x_para[s_])

            # Calculate right hand summation
            c = 0
            for s in self.BP.states:
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        c += self.BP.T(s, a, s_)*self.in_y[s][a]
            
            c = self.gamma*c

            # Calculate right hand side
            if s_ in self.belief_state:
                c += 1/len(self.belief_state)

            # Adding constraint
            self.constraints.append(c <= y + self.s1[s_])

    def make_constraints_eqn2(self):
        for s_ in self.BP.states:
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)
            y = cp.exp(self.x[s_])

            # Calculate right hand summation
            c = 0
            for s in self.BP.states:
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        c += self.BP.T(s, a, s_)*self.in_y_para[s][a]*(1 + self.x[s] + self.pi[s][a] - self.x_para[s] - self.pi_para[s][a])
            
            c = self.gamma*c

            # Calculate right hand side
            if s_ in self.belief_state:
                c += 1/len(self.belief_state)

            # Adding constraint
            self.constraints.append(y <= c + self.s2[s_])

    def make_constraints_eqn3(self):
        for s in self.BP.states:
            self.constraints.append(self.s1[s] >= 0)
            self.constraints.append(self.s2[s] >= 0)

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
            self.prob.solve(solver=cp.SCS, verbose=True)
        except Exception as e:
            print(e)

    def solve_DCP(self, name):
        with open('csv_' + name + '.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["iteration", "V"])
            for i in range(30):
                self.tao.value = min(self.mu*self.tao.value, self.tao_max)
                self.solve_prob()
                csvwriter.writerow([i, self.prob.value])
                self.save_policy(name + '_' + str(i))
                self.change_para()

    def save_policy(self, name):
        pi_ = {}
        pi_max = {}
        x_ = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            pi_[s] = {}
            ma = 0
            for a in actions:
                pi_[s][a] = self.pi[s][a].value
                if(pi_[s][a] > ma):
                    pi_max[s] = a
                    ma = pi_[s][a]

        with open('policy/'+ 'Planning_Agent_Policy_' + name + '.pkl', 'wb') as f:
            pickle.dump(pi_, f)

        with open('policy/'+ 'Planning_Agent_Policy_' + name + '_max' + '.pkl', 'wb') as f:
            pickle.dump(pi_max, f)

        for s in self.BP.states:
            x_[s] = self.x[s].value

        with open('policy/'+ 'Planning_Agent_x_' + name + '.pkl', 'wb') as f:
            pickle.dump(x_, f)

        for s in self.BP.states:
            x_[s] = self.s1[s].value
            
        with open('policy/'+ 'Planning_Agent_s1_' + name + '.pkl', 'wb') as f:
            pickle.dump(x_, f)
        
        for s in self.BP.states:
            x_[s] = self.s2[s].value
            
        with open('policy/'+ 'Planning_Agent_s2_' + name + '.pkl', 'wb') as f:
            pickle.dump(x_, f)

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    
    locations = [(int(int(sys.argv[1])/2), 1)]

    # if int(sys.argv[1]) == 7:
    #     locations=[(3, 0), (6, 3), (0, 3), (1, 2), (5, 4)]
    # BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = PlanningAgent(BP, locations=locations)
    agent.solve_DCP(sys.argv[8])