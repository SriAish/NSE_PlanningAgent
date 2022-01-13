from misc import BoxPushingConstants
import sys
import pickle
from gekko import GEKKO
from math import e, log

class NCAgent:
    def __init__(self, BP, gamma = 0.9, locations = None):
        self.m = GEKKO(remote=False)
        self.m.options.IMODE = 3
        self.m.options.SOLVER = int(sys.argv[9])
        self.BP = BP
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.locations = locations
        self.init_belief()
        print("initial belief setup")
        sys.stdout.flush()
        self.init_var()
        print("variables setup")
        sys.stdout.flush()
        self.init_intermediates()
        self.make_prob()
        print("problem setup")
        sys.stdout.flush()
    
    def load(self, name):
        file_to_read = open(name, "rb")
        return pickle.load(file_to_read)

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
        for s in self.BP.states:
            self.pi[s] = {}
            self.x[s] = self.m.Var()
            actions = self.BP.getValidActions(s)
            val = log(1/len(actions))
            for a in actions:
                self.pi[s][a] = self.m.Var(val)

    def init_intermediates(self):
        self.in_y = {}
        for s in self.BP.states:
            self.in_y[s] = {} 
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.in_y[s][a] = self.m.Intermediate(e**self.x[s]*e**self.pi[s][a])

    def set_obj(self):
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.m.Minimize(self.in_y[s][a]*self.BP.get_cost(s, a))

    def pr_obj(self):
        obj = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                obj += (e**self.x[s].value[0])*(e**self.pi[s][a].value[0])*self.BP.get_cost(s, a)
        return obj

    def make_constraints_eqn1(self):
        for s_ in self.BP.states:
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)
            # y = self.x[s_]
            y = 0
            for a in actions:
                y += self.in_y[s_][a]

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
            self.m.Equation(y == c)
    
    def make_constraints_eqn2(self):
        su = 1
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            c = 0
            for a in actions:
                c += e**self.pi[s][a]
            if actions:
                self.m.Equation(c == su)


    def make_constraints_eqn3(self):
        trajs = self.load('severe_trajectories_7')
        lhs = 0
        for t in trajs:
            e_pow = 0
            tra = 1
            ele = 0
            for s, a in t:
                e_pow += self.x[s] + self.pi[s][a]
                if ele == 0:
                    ele += 1
                else:
                    tra = tra*self.BP.T(s_prev, a_prev, s)
                s_prev = s
                a_prev = a

            lhs += (e**e_pow)*tra

        self.m.Equation(lhs <= 1)

    
    def nse_sum(self):
        trajs = self.load('severe_trajectories_7')
        lhs = 0
        for t in trajs:
            e_pow = 1
            tra = 1
            ele = 0
            for s, a in t:
                e_pow *= e**self.x[s].value[0] * e**self.pi[s][a].value[0]
                if ele == 0:
                    ele += 1
                else:
                    tra = tra*self.BP.T(s_prev, a_prev, s)
                s_prev = s
                a_prev = a

            lhs += e_pow*tra

        trajs = self.load('mild_trajectories_7')

        ans = lhs
        lhs = 0
        for t in trajs:
            e_pow = 1
            tra = 1
            ele = 0
            for s, a in t:
                e_pow *= e**self.x[s].value[0] * e**self.pi[s][a].value[0]
                if ele == 0:
                    ele += 1
                else:
                    tra = tra*self.BP.T(s_prev, a_prev, s)
                s_prev = s
                a_prev = a

            lhs += e_pow*tra

        return ans, lhs

    def make_constraints_eqn4(self):
        trajs = self.load('mild_trajectories_7')
        lhs = 0
        for t in trajs:
            e_pow = 0
            tra = 1
            ele = 0
            for s, a in t:
                e_pow += self.x[s] + self.pi[s][a]
                if ele == 0:
                    ele += 1
                else:
                    tra = tra*self.BP.T(s_prev, a_prev, s)
                s_prev = s
                a_prev = a

            lhs += (e**e_pow)*tra

        self.m.Equation(lhs <= 0.5)


    def make_constraints_eqn5(self):
        lhs = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                lhs += self.in_y[s][a]*self.BP.get_cost(s, a)

        self.m.Equation(lhs - 8.2 <= 2)

    def make_prob(self):
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        self.make_constraints_eqn2()
        print("eq2")
        self.make_constraints_eqn3()
        print("eq3")
        self.make_constraints_eqn4()
        print("eq4")
        self.make_constraints_eqn5()
        print("eq5")
        sys.stdout.flush()

    def calculate_pi(self):
        print("----------------------------------------")
        print("Objective Value: ", self.pr_obj())
        print("Objective Value: ", self.nse_sum())
        print("----------------------------------------")
        self.pi_ = {}
        self.x_ = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            self.pi_[s] = {}
            self.x_[s] = e**self.x[s].value[0]
            for a in actions:
                self.pi_[s][a] = e**self.pi[s][a].value[0]
            print(s, self.x_[s])
            print(self.pi_[s])

    def save_pi(self, file):
        print("Saving policies")
        with open('policy/'+ 'NC_Agent_Policy_fc_' + sys.argv[9] + '_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.pi_, f)

        with open('policy/'+ 'NC_Agent_x_fc_' + sys.argv[9] + '_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.x_, f)

    def solve_prob(self):
        try:
            self.m.solve(debug=0)
        except Exception as e:
            print("Exception Occured")
            print(e)

if __name__ == '__main__':
    g_pos = (int(sys.argv[6]), int(sys.argv[7]))
    e_state = (g_pos, g_pos, False, 'p')
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
    
    locations = [(int(int(sys.argv[1])/2), 1)]

    # if int(sys.argv[1]) == 7:
    #     locations=[(3, 0), (6, 3), (0, 3), (1, 2), (5, 4)]
    # BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = NCAgent(BP, locations=locations)
    agent.solve_prob()
    agent.calculate_pi()
    agent.save_pi(sys.argv[8])