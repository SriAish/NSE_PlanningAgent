from misc import BoxPushingConstants
import sys
import pickle
import cvxpy as cp

class DLPAgent:
    def __init__(self, BP, gamma = 0.9, locations = None):
        self.BP = BP
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.locations = locations
        self.init_belief()
        self.check_states()
        print("initial belief setup")
        sys.stdout.flush()
        self.init_var()
        print("variables setup")
        sys.stdout.flush()
        self.make_prob()
        print("problem setup")
        sys.stdout.flush()
    
    def check_states(self):
        self.check_state = []
        self.check_state.append(((0,0), (1,1), False, 'p'))
        self.check_state.append(((0,1), (1,1), False, 'p'))
        self.check_state.append(((1,1), (1,1), False, 'p'))
        self.check_state.append(((1,1), (1,1), True, 'p'))
        self.check_state.append(((2, 1), (2, 1), True, 'p'))
        self.check_state.append(((2, 2), (2, 2), True, 'p'))
        self.check_state.append(((2, 2), (2, 2), False, 'p'))
    
    def init_belief(self):
        if self.locations == None:
            self.locations = [(1, 1)]
        init_loc = (0, 0)
        self.belief_state = []
        for i in self.locations:
            self.belief_state.append((init_loc, i, False, 'p'))

    def init_var(self):
        self.y = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.y[(s, a)] = cp.Variable(nonneg=True)

    def set_obj(self):
        obj = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                obj += self.y[(s, a)]*self.BP.get_cost(s, a)

        self.obj = cp.Minimize(obj)

    def make_constraints_eqn1(self):
        for s_ in self.BP.states:
            if(s_ in self.check_state):
                print("--------------------------")
                print(s_)
            # Calculate left hand side
            actions = self.BP.getValidActions(s_)
            y = 0
            for a_ in actions:
                if(s_ in self.check_state):
                    print(a_)
                y += self.y[(s_, a_)]

            # Calculate right hand summation
            c = 0
            for s in self.BP.states:
                actions = self.BP.getValidActions(s)
                for a in actions:
                    if self.BP.T(s, a, s_) != 0:
                        if(s_ in self.check_state):
                            print(s, a, self.BP.T(s, a, s_))
                        c += (self.BP.T(s, a, s_)*(self.y[(s, a)]))
            
            c = self.gamma*c

            # Calculate right hand side
            if s_ in self.belief_state:
                c += 1/len(self.belief_state)
                print(s_, 1/len(self.belief_state))


            if(s_ in self.check_state):
                print("--------------------------")
            # Adding constraint
            self.constraints.append(y == c)
    
    def make_constraints_eqn2(self):
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                self.constraints.append(self.y[(s, a)] >= 0)

    def make_prob(self):
        self.constraints = []
        self.set_obj()
        print("objective setup")
        sys.stdout.flush()
        self.make_constraints_eqn1()
        print("eq1")
        sys.stdout.flush()
        # self.make_constraints_eqn2()
        # print("eq2")
        # sys.stdout.flush()
        self.prob = cp.Problem(self.obj, self.constraints)

    def calculate_pi(self):
        print("----------------------------------------")
        print("Objective Value: ", self.prob.value)
        print("----------------------------------------")
        self.pi = {}
        self.pi_max = {}
        self.y_ = {}
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            self.pi[s] = {}
            y = 0
            ma = 0
            for a in actions:
                self.y_[(s, a)] = self.y[(s, a)].value
                y += self.y_[(s, a)]
                if(self.y_[(s,a)] > ma):
                    self.pi_max[s] = a
                    ma = self.y_[(s,a)]

            for a in actions:
                self.pi[s][a] = self.y_[(s,a)]/y

    def save_pi(self, file):
        print("Saving policies")
        with open('policy/'+ 'DLP_Agent_Policy_' + file + '.pkl', 'wb') as f:
            pickle.dump(self.pi, f)

        with open('policy/'+ 'DLP_Agent_Policy_' + file + '_max' + '.pkl', 'wb') as f:
            pickle.dump(self.pi_max, f)

        with open('policy/'+ 'DLP_Agent_Policy_' + file + 'y' + '.pkl', 'wb') as f:
            pickle.dump(self.y_, f)

    def solve_prob(self):
        try:
            self.prob.solve(solver=cp.SCS)
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