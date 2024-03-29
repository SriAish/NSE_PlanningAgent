from EnvConst import BoxPushingConstants
from makeFSA import FSAConstants
import sys
import pickle
import itertools
from gekko import GEKKO
from math import e
from misc import load

class FSAgent:
    def __init__(self, BP, FSA, gamma = 0.99, locations = None):
        self.m = GEKKO(remote=False)
        self.m.options.MAX_ITER = 3000
        self.m.options.SOLVER = int(sys.argv[10])
        self.BP = BP
        self.FSA = FSA
        self.gamma = gamma
        self.locations = locations
        self.init_belief()
        print("initial belief setup")
        sys.stdout.flush()
        self.init_var()
        print("variables setup")
        sys.stdout.flush()
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
            s = (init_loc, i, False, False, 'p')
            self.belief_state.append((self.FSA.nextState('0', s, "emp"), s))
        print("belief:", self.belief_state)

    def init_var(self):
        self.x = {}
        self.pi = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for u in self.FSA.states:
                self.pi[(u, s)] = {}
                for a in actions:
                    self.x[(u, s, a)] = self.m.Var(lb=0, ub=1/(1-self.gamma))
    
    def set_obj(self):
        for u, s in itertools.product(self.FSA.states, self.BP.states):
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.m.Minimize(self.x[(u, s, a)]*self.BP.getCost(s, a))

    def pr_obj(self):
        obj = 0
        for u, s in itertools.product(self.FSA.states, self.BP.states):
            actions = self.BP.getValidActions(s)
            for a in actions:
                obj += self.x_[(u, s)]*self.pi_[(u, s)][a]*self.BP.getCost(s, a)
        return obj

    def set_bound(self):
        obj = 0
        i = 0
        o = 0
        for u, s in itertools.product(self.FSA.states, self.BP.states):
            actions = self.BP.getValidActions(s)
            for a in actions:
                i += 1
                o += self.x[(u, s, a)]*self.BP.getCost(s, a)
            if i%200 == 0:
                obj += self.m.Intermediate(o)
                o = 0
        obj += self.m.Intermediate(o)
        self.m.Equation(obj - 4.2598 <= 5)

    def make_constraints_eqn1(self):
        for u_, s_ in itertools.product(self.FSA.states, self.BP.states):
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)

            y = 0
            for a in actions:
                y += self.x[(u_, s_, a)]

            # Calculate right hand summation
            c = 0
            for u, s in itertools.product(self.FSA.states, self.BP.states):
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        if self.FSA.T(u, s_, a, u_) != 0:
                            c += self.BP.T(s, a, s_)*self.FSA.T(u, s_, a, u_)*self.x[(u, s, a)]
            
            c = self.gamma*c

            # Calculate right hand side
            if (u_, s_) in self.belief_state:
                c += 1/len(self.belief_state)

            # Adding constraint
            self.m.Equation(y == c)

    def make_constraints_eqn3(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        t = self.FSA.symbolT(u, s_, a, self.FSA.symbols["severe"])
                        if t != 0:
                            lhs += self.x[(u, s, a)]*self.BP.T(s, a, s_)*t
        
        self.m.Equation(lhs <= float(sys.argv[11]))

    def make_constraints_eqn4(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        t = self.FSA.symbolT(u, s_, a, self.FSA.symbols["mild"])
                        if t != 0:
                            lhs += self.x[(u, s, a)]*self.BP.T(s, a, s_)*t
        
        self.m.Equation(lhs <= float(sys.argv[12]))

    def NSE_val(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
               
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        t = self.FSA.symbolT(u, s_, a, self.FSA.symbols["severe"])
                        if t != 0:
                            l = self.x_[(u, s)]*self.pi_[(u, s)][a]*self.BP.T(s, a, s_)*t
                            lhs += l
        
        return lhs

    def NSE_val_mild(self):
        lhs = 0
        for s_ in self.BP.states:
            for u, s in itertools.product(self.FSA.states, self.BP.states):
               
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        t = self.FSA.symbolT(u, s_, a, self.FSA.symbols["mild"])
                        if t != 0:
                            l = self.x_[(u, s)]*self.pi_[(u, s)][a]*self.BP.T(s, a, s_)*t
                            lhs += l
        
        return lhs

    def make_prob(self):
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        sys.stdout.flush()
        self.set_bound()
        print("setting bound")
        sys.stdout.flush()
        if float(sys.argv[10]) >= 0:
            self.make_constraints_eqn3()
            print("eq3")
            sys.stdout.flush()
        # if float(sys.argv[11]) >= 0:
        #     self.make_constraints_eqn4()
        #     print("eq4")
        #     sys.stdout.flush()

    def calculate_pi(self):
        self.pi_ = {}
        self.x_ = {}
        for u, s in itertools.product(self.FSA.states, self.BP.states):
            actions = self.BP.getValidActions(s)
            self.pi_[(u, s)] = {}
            self.x_[(u, s)] = 0
            for a in actions:
                self.x_[(u, s)] += self.x[(u, s, a)].value[0]
            
            for a in actions:
                if self.x_[(u, s)] > 0:
                    self.pi_[(u, s)][a] = self.x[(u, s, a)].value[0]/self.x_[(u, s)]
                else:
                    self.pi_[(u, s)][a] = 1/len(actions)
            if self.x_[(u, s)] > 0.00001:
                print((u, s), self.x_[(u, s)])
                print(self.pi_[(u, s)])

        print("----------------------------------------")
        print("Objective Value: ", self.pr_obj())
        print("Severe Value: ", self.NSE_val())
        # print("Mild Value: ", self.NSE_val_mild())
        print("----------------------------------------")

    def save_pi(self, file):
        print("Saving policies")
        with open('policy/'+ 'FSA_LP_p' + sys.argv[10] + '_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.pi_, f)

        with open('policy/'+ 'FSA_LP_x' + sys.argv[10] + '_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.x_, f)

    def solve_prob(self):
        try:
            self.m.solve(disp=True)
        except Exception as e:
            print("Exception Occured")
            print(e)

if __name__ == '__main__':
    g_pos = (int(sys.argv[7]), int(sys.argv[8]))
    g_state = [(g_pos, g_pos, True, False, 'p'), (g_pos, g_pos, True, True, 'p')]
    BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), (int(sys.argv[5]), int(sys.argv[6])), g_state)
    file_name = sys.argv[13][sys.argv[13].index("/")+1:]
    delta = load("results/delta/new_" + file_name + "_" + sys.argv[14] + "_best")
    omega = load("results/omega/new_" + file_name + "_" + sys.argv[14] + "_best")
    FSA = FSAConstants(delta, omega)
    # locations = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 5), (3, 1), (3, 5), (4, 1), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
    # locations = [(3, 0), (1, 2), (0, 3), (6, 3), (5, 4)]
    locations = [(0, 1)]

    if int(sys.argv[1]) == 3:
        locations = [(0, 1)]
        # locations=[(3, 0), (6, 3), (0, 3), (1, 2), (5, 4)]
    # BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = FSAgent(BP, FSA, locations=locations)
    agent.solve_prob()
    agent.calculate_pi()
    agent.save_pi(sys.argv[9])