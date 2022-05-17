from misc import BoxPushingConstants
import sys
import pickle
from math import e
import csv

class NCAgent:
    def __init__(self, BP, gamma = 0.9, locations = None):
        self.BP = BP
        self.no_states = len(self.BP.states)
        self.gamma = gamma
        self.locations = locations
        self.init_belief()
        self.init_var()
    
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
        self.x = self.load('policy/NC_Agent_x_nor_3_7_7_ogt.pkl')
        self.pi = self.load('policy/NC_Agent_Policy_nor_3_7_7_ogt.pkl')

    def nse_sum(self):
        sa = self.load('state_action_NSE')
        nse = 0
        for s in self.BP.states:
            actions = self.BP.getValidActions(s)
            for a in actions:
                if (s,a) in sa:
                    nse += self.x[s]*self.pi[s][a]*sa[(s,a)]

        return nse

    def calculate_pi(self):
        print("----------------------------------------")
        print("Trajectory Value: ", self.nse_sum())
        print("----------------------------------------")

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
    
    locations = [(3, 0), (1, 2), (0, 3), (6, 3), (5, 4)]

    # if int(sys.argv[1]) == 7:
    #     locations=[(3, 0), (6, 3), (0, 3), (1, 2), (5, 4)]
    # BP = BoxPushingConstants(7, 3, 3, (2, 2), ((3, 6), (3, 6), False, 'p'))
    agent = NCAgent(BP, locations=locations)
    agent.calculate_pi()