from misc import BoxPushingConstants
import sys
import pickle
from gekko import GEKKO
from math import e

class DLPAgent:
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
            self.x[s] = self.m.Var()
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.pi[s][a] = self.m.Var()

    def init_intermediates(self):
        self.in_y = {}
        for s in self.BP.states:
            self.in_y[s] = {} 
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.in_y[s][a] = e**(self.x[s] + self.pi[s][a])

    def set_obj(self):
        obj = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.m.Minimize(self.in_y[s][a]*self.BP.get_cost(s, a))

    def make_constraints_eqn1(self):
        for s_ in self.BP.states:
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)
            y = e**self.x[s_]

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
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.constraints.append(e**(self.x[s] + self.pi[s][a]) >= 0)

    def make_prob(self):
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        sys.stdout.flush()

    def calculate_pi(self):
        print("----------------------------------------")
        print("Objective Value: ", m.options.OBJFCNVAL)
        print("----------------------------------------")
        self.pi_ = {}
        self.pi_max = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            self.pi_[s] = {}
            ma = 0
            for a in actions:
                self.pi_[s][a] = self.pi[s][a].value[0]
                if(self.pi_[s][a] > ma):
                    self.pi_max[s] = a

    def save_pi(self, file):
        print("Saving policies")
        with open('policy/'+ 'NC_Agent_Policy_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.pi_, f, pickle.HIGHEST_PROTOCOL)

        with open('policy/'+ 'NC_Agent_Policy_' + file + '_max' + '.pkl', 'wb') as f:
            pickle.dump(self.pi_max, f, pickle.HIGHEST_PROTOCOL)

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
    agent = DLPAgent(BP, locations=locations)
    agent.solve_prob()
    agent.calculate_pi()
    agent.save_pi(sys.argv[8])