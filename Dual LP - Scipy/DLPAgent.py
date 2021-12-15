import numpy as np
from scipy.optimize import minimize
from misc import BoxPushingConstants
import sys
import pickle
from math import e, gamma

# Declare environment variables
g_pos = (int(sys.argv[6]), int(sys.argv[7]))
e_state = (g_pos, g_pos, False, 'p')
BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)

locations = [(int(int(sys.argv[1])/2), 1)]

def init_belief(locations):
    init_loc = (0, 0)
    belief_state = []
    for i in locations:
        belief_state.append((init_loc, i, False, 'p'))
    return belief_state

belief_state = init_belief(locations)
gamma = 0.9

# Variables for scipy optimization
no_of_states = len(BP.states)
no_of_actions = 6

state_to_index = {}
action_to_index = {}

i = 0
for state in BP.states:
    state_to_index[state] = i*no_of_actions
    i += 1

i = 0
for action in BP.actions.allActions:
    action_to_index[action] = i
    i += 1

def constraint_spec(state_):
    def contraint(y):
        # LHS
        s_ = state_to_index[state_]
        lhs = 0
        actions = BP.getValidActions(state_)
        for action in actions:
            lhs += y[s_ + action_to_index[action]]
        
        # RHS
        rhs = 0
        for state in BP.states:
            s = state_to_index[state]
            actions = BP.getValidActions(state)
            for action in actions:
                if BP.T(state, action, state_) != 0:
                    rhs += y[s + action_to_index[action]]*BP.T(state, action, state_)
            
        rhs = gamma*rhs
        
        if state_ in belief_state:
            rhs += 1/len(belief_state)

        return lhs - rhs

    return contraint

def constraint_spec2(state, action):
    def constraint(y):
        return y[state_to_index[state] + action_to_index[action]]

    return constraint

def obj(y):
    obj = 0
    for state in BP.states:
        s = state_to_index[state]
        actions = BP.getValidActions(state)
        for action in actions:
            obj += y[s + action_to_index[action]]*BP.get_cost(state, action)

    return obj

# initial guess
x0 = np.zeros(no_of_states*no_of_actions)

# bound
b = (0, 1/(1-gamma))
bnds = (b * (no_of_states*no_of_actions))

# show initial objective
print('Initial SSE Objective: ' + str(obj(x0)))

# optimize 
cons = []
for state in BP.states:
    actions = BP.getValidActions(state)
    cons.append({'type': 'eq', 'fun': constraint_spec(state)})
    # for action in actions:
    #     cons.append({'type': 'ineq', 'fun': constraint_spec2(state, action)})

cons = (cons)

solution = minimize(obj, x0, method='SLSQP', bounds=bnds, constraints=cons)

x = solution.x
# show final objective
print('Final SSE Objective: ' + str(obj(x)))

with open('policy/'+ 'DLP_Agent_state_ind_' + sys.argv[8] + '.pkl', 'wb') as f:
    pickle.dump(state_to_index, f)

with open('policy/'+ 'DLP_Agent_action_ind_' + sys.argv[8] + '.pkl', 'wb') as f:
    pickle.dump(action_to_index, f)

with open('policy/'+ 'DLP_Agent_Policy_' + sys.argv[8] + '.pkl', 'wb') as f:
    pickle.dump(x, f)