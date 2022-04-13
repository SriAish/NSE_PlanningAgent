import numpy as np
from scipy.optimize import minimize
from EnvConst import BoxPushingConstants
from FSAConst import FSAConstants
import sys
import pickle
import itertools

# Declare environment variables
g_pos = (int(sys.argv[6]), int(sys.argv[7]))
g_state = [(g_pos, g_pos, True, False, 'p'), (g_pos, g_pos, True, True, 'p')]
BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), g_state)
FSA = FSAConstants()

locations = [(3, 0)]

def init_belief(locations):
    init_loc = (0, 0)
    belief_state = []
    for i in locations:
        belief_state.append(("u1", (init_loc, i, False, False, 'p')))
    return belief_state

belief_state = init_belief(locations)
gamma = 0.999

# Variables for scipy optimization
no_of_states = len(BP.states)*len(FSA.states)
no_of_actions = len(BP.actions.all_actions)

state_to_index = {}
action_to_index = {}

i = 0
for u, s in itertools.product(FSA.states, BP.states):
    state_to_index[(u, s)] = i*no_of_actions
    i += 1

i = 0
for action in BP.actions.all_actions:
    action_to_index[action] = i
    i += 1

def constraint_spec(state_):
    def contraint(y):
        # LHS
        s_ = state_to_index[state_]
        lhs = 0
        actions = BP.getValidActions(state_[1])
        for action in actions:
            lhs += y[s_ + action_to_index[action]]
        
        # RHS
        rhs = 0
        for u, state in itertools.product(FSA.states, BP.states):
            s = state_to_index[(u, state)]
            actions = BP.getValidActions(state)
            for action in actions:
                if BP.T(state, action, state_[1]) != 0:
                    if FSA.T(u, state_[1], action, state_[0]) != 0:
                        rhs += y[s + action_to_index[action]]*BP.T(state, action, state_[1])*FSA.T(u, state_[1], action, state_[0])
            
        rhs = gamma*rhs
        
        if state_ in belief_state:
            rhs += 1/len(belief_state)

        return lhs - rhs

    return contraint

def constraint_spec2(state):
    def constraint(y):
        return y[state_to_index[state] + action_to_index[action]]

    return constraint

def obj(y):
    obj = 0
    for u, state in itertools.product(FSA.states, BP.states):
        actions = BP.getValidActions(state)
        for action in actions:
            obj += y[state_to_index[(u, state)] + action_to_index[action]]*BP.getCost(state, action)

    return obj

# initial guess
len_of_x = no_of_states*no_of_actions
x0 = np.zeros(len_of_x)

# bound
b = (0, 1/(1-gamma))
bnds = ((b, ) * len_of_x)

# show initial objective
print('Initial SSE Objective: ' + str(obj(x0)))

# optimize 
cons = []
for u, state in itertools.product(FSA.states, BP.states):
    actions = BP.getValidActions(state)
    cons.append({'type': 'eq', 'fun': constraint_spec((u, state))})
    # for action in actions:
    #     cons.append({'type': 'ineq', 'fun': constraint_spec2(state, action)})

cons = (cons)
solution = minimize(obj, x0, method='SLSQP', bounds=bnds, constraints=cons)

x = solution.x
# show final objective
print('Final SSE Objective: ' + str(obj(x)))

# with open('policy/'+ 'DLP_Agent_SLSQP_with_upper_state_ind_' + sys.argv[8] + '.pkl', 'wb') as f:
#     pickle.dump(state_to_index, f)

# with open('policy/'+ 'DLP_Agent_SLSQP_with_upper_action_ind_' + sys.argv[8] + '.pkl', 'wb') as f:
#     pickle.dump(action_to_index, f)

# with open('policy/'+ 'DLP_Agent_SLSQP_with_upper_Policy_' + sys.argv[8] + '.pkl', 'wb') as f:
#     pickle.dump(x, f)