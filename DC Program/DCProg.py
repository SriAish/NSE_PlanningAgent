from misc import BoxPushingConstants
import sys
import pickle
import cvxpy as cp
from math import e, log

class DCProg:
    def __init__(self, BP, gamma = 0.9, locations = None):
        self.BP = BP
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.locations = locations
        self.tao = cp.Parameter()
        self.tao.value = 1
        self.mu = 10
        self.tao_max = 1000000
        self.init_belief()
        print("initial belief setup")
        sys.stdout.flush()
        self.init_var()
        print("variables setup")
        sys.stdout.flush()
        self.init_para()
        print("parameters setup")
        sys.stdout.flush()
        self.init_intermediates()
        print("intermediates setup")
        sys.stdout.flush()
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
        self.slack = {}
        for s in self.BP.states:
            self.x[s] = cp.Variable()
            self.pi[s] = {}
            self.slack[s] = cp.Variable(4, nonneg=True)
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.pi[s][a] = cp.Variable()


    def init_para(self):
        self.x_para = {}
        self.pi_para = {}
        for s in self.BP.states:
            self.x_para[s] = cp.Parameter()
            self.x_para[s].value = 0
            self.pi_para[s] = {}
            actions = self.BP.getValidActions(s)
            val = log(1/len(actions))
            for a in actions:
                self.pi_para[s][a] = cp.Parameter()
                self.pi_para[s][a].value = val


    def init_intermediates(self):
        self.y = {}
        self.y_para = {}
        for s in self.BP.states:
            self.y[s] = {} 
            self.y_para[s] = {}
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.y[s][a] = cp.exp(self.x[s] + self.pi[s][a])
                self.y_para[s][a] = cp.exp(self.x_para[s] + self.pi_para[s][a])


    def change_para(self):
        for s in self.BP.states:
            self.x_para[s].value = self.x[s].value
            for a in self.pi[s]:
                self.pi_para[s][a].value = self.pi[s][a].value


    def set_obj(self):
        obj = 0
        slack = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                obj += self.y[s][a]*self.BP.get_cost(s, a)
            slack += cp.sum(self.slack[s])

        self.obj = cp.Minimize(obj + (self.tao*slack))


    def make_constraints_eqn1(self):
        for s_ in self.BP.states:
            # Calculate right hand side
            actions = self.BP.getValidActions(s_)
            rhs = 0
            for a_ in actions:
                rhs += self.y_para[s_][a_]*(1 + self.x[s_] + self.pi[s_][a_] - self.x_para[s_] - self.pi_para[s_][a_])

            # Calculate left hand summation
            lhs = 0
            for s in self.BP.states:
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        lhs += self.BP.T(s, a, s_)*self.y[s][a]
            
            lhs = self.gamma*lhs

            # Calculate left hand side
            if s_ in self.belief_state:
                lhs += 1/len(self.belief_state)

            # Adding constraint
            self.constraints.append(lhs <= rhs + self.slack[s_][0])


    def make_constraints_eqn2(self):
        for s_ in self.BP.states:
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)
            lhs = 0
            for a_ in actions:
                lhs += self.y[s_][a_]

            # Calculate right hand summation
            rhs = 0
            for s in self.BP.states:
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        rhs += self.BP.T(s, a, s_)*self.y_para[s][a]*(1 + self.x[s] + self.pi[s][a] - self.x_para[s] - self.pi_para[s][a])
            
            rhs = self.gamma*rhs

            # Calculate right hand side
            if s_ in self.belief_state:
                rhs += 1/len(self.belief_state)

            # Adding constraint
            self.constraints.append(lhs <= rhs + self.slack[s_][1])


    def make_constraints_eqn3(self):
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            a_sum = 0
            for a in actions:
                a_sum += cp.exp(self.pi_para[s][a])*(1 + self.pi[s][a] - self.pi_para[s][a])

            self.constraints.append(1 <= a_sum + self.slack[s][2])


    def make_constraints_eqn4(self):
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            a_sum = 0
            for a in actions:
                a_sum += cp.exp(self.pi[s][a])

            self.constraints.append(a_sum <= 1 + self.slack[s][3])
                

    def make_prob(self):
        self.constraints = []
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        self.make_constraints_eqn2()
        print("eq1")
        self.make_constraints_eqn3()
        print("eq1")
        self.make_constraints_eqn4()
        print("eq1")
        sys.stdout.flush()
        self.prob = cp.Problem(self.obj, self.constraints)


    def calculate_pi(self):
        # print("----------------------------------------")
        # print("Objective Value: ", self.prob.value)
        # print("----------------------------------------")
        self.pi_v = {}
        self.x_v = {}
        for s in self.BP.states:
            print(s, " : ", e**self.x[s].value)
            actions = self.BP.getValidActions(s)
            self.x_v[s] = self.x[s].value
            self.pi_v[s] = {}
            for a in actions:
                self.pi_v[s][a] = e**self.pi[s][a].value
            print(self.pi_v[s])
            print("----------------------------------------")

    def save(self, file):
        print("Saving policies")
        with open('policy/'+ 'DC_x_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.x_v, f)

        with open('policy/'+ 'DC_pi_' + file + '_max' + '.pkl', 'wb') as f:
            pickle.dump(self.pi_v, f)


    def solve_prob(self):
        try:
            self.prob.solve(solver=cp.SCS)
        except Exception as e:
            print("Exception Occured")
            print(e)


    def solve_DCP(self):
        obj_val = sys.maxsize
        delta = sys.maxsize
        i = 0
        while delta > 0.001:
            self.tao.value = min(self.mu*self.tao.value, self.tao_max)
            self.solve_prob()
            # self.calculate_pi()
            # self.save(sys.argv[8])
            print(i)
            print(self.prob.value)
            delta = abs(self.prob.value - obj_val)
            print(delta)
            sys.stdout.flush()
            obj_val = self.prob.value
            self.change_para()
            i += 1

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    
    locations = [(int(int(sys.argv[1])/2), 1)]

    # if int(sys.argv[1]) == 7:
    #     locations=[(3, 0), (6, 3), (0, 3), (1, 2), (5, 4)]
    # BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = DCProg(BP, locations=locations)
    agent.solve_DCP()
    # agent.calculate_pi()
    # agent.save_pi(sys.argv[8])