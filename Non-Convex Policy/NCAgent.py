from misc import BoxPushingConstants
import sys
import pickle
from gekko import GEKKO
from math import e

class NCAgent:
    def __init__(self, BP, gamma = 0.9, locations = None):
        self.m = GEKKO()
        self.m.options.IMODE = 3
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
            self.x[s] = self.m.Var(lb=0)
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.pi[s][a] = self.m.Var(1/len(actions), lb=0, ub=1)

    def init_intermediates(self):
        self.in_y = {}
        for s in self.BP.states:
            self.in_y[s] = {} 
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.in_y[s][a] = self.x[s]*self.pi[s][a]

    def set_obj(self):
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.m.Minimize(self.in_y[s][a]*self.BP.get_cost(s, a))

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

    def make_prob(self):
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        self.make_constraints_eqn2()
        print("eq2")
        sys.stdout.flush()

    def calculate_pi(self):
        print("----------------------------------------")
        print("Objective Value: ", self.m.options.OBJFCNVAL)
        print("----------------------------------------")
        self.pi_ = {}
        self.pi_max = {}
        self.x_ = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            self.pi_[s] = {}
            self.x_[s] = self.x[s].value[0]
            ma = 0
            for a in actions:
                self.pi_[s][a] = self.pi[s][a].value[0]
                if(ma == 0):
                    ma = self.pi_[s][a]
                    self.pi_max[s] = a
                elif(self.pi_[s][a] > ma):
                    self.pi_max[s] = a
                    ma = self.pi_[s][a]

    def save_pi(self, file):
        print("Saving policies")
        with open('policy/'+ 'NC_Agent_Policy_init_fc_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.pi_, f)

        with open('policy/'+ 'NC_Agent_Policy_init_fc_' + file + '_max' + '.pkl', 'wb') as f:
            pickle.dump(self.pi_max, f)

        with open('policy/'+ 'NC_Agent_x_init_fc_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.x_, f)

    def solve_prob(self):
        try:
            self.m.solve()
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