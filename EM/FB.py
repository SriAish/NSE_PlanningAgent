from re import S
from tracemalloc import start


class FB:
    def __init__(self, delta, omega, states, R, st = '0', end = '#'):
        self.delta = delta
        self.omega = omega
        self.start = st
        self.end = end
        self.states = states
        self.R = R
        self.forward_step = {}
        self.backward_step = {}
        self.gamma_val = {}
        self.eta_val = {}

        for r in range(len(R)):
            self.forward_step[r] = {}
            self.backward_step[r] = {}
            self.gamma_val[r] = {}
            self.eta_val[r] = {}


    def alpha(self, r, t, u):
        if t in self.forward_step[r] and u in self.forward_step[r][t]:
            return self.forward_step[r][t][u]
        
        if t not in self.forward_step[r]:
            self.forward_step[r][t] = {}

        if t == 0:
            self.forward_step[r][t][u] = self.delta[self.start][self.R[r][t]][u]
            return self.forward_step[r][t][u]

        ba = 0
        for s in self.states:
            ba += self.alpha(r, t-1, s)*self.delta[s][self.R[r][t]][u]
        self.forward_step[r][t][u] = ba
        
        return self.forward_step[r][t][u]

    def beta(self, r, t, u):
        if t in self.backward_step[r] and u in self.backward_step[r][t]:
            return self.backward_step[r][t][u]
        
        if t not in self.backward_step[r]:
            self.backward_step[r][t] = {}

        if t == len(self.R[r]) - 3:
            # print(self.delta[u][self.R[r][t+1]][self.end], self.omega[u][self.R[r][t+1]][self.R[r][t + 2]])
            self.backward_step[r][t][u] = self.delta[u][self.R[r][t+1]][self.end]*self.omega[u][self.R[r][t+1]][self.R[r][t + 2]]
            # print(self.backward_step[r][t][u])
            return self.backward_step[r][t][u]

        if t > len(self.R[r]) - 3:
            raise Exception("Time step value exceeds number of time steps.")

        fo = 0
        for s in self.states:
            fo += self.beta(r, t+1, s)*self.delta[u][self.R[r][t+1]][s]
        self.backward_step[r][t][u] = fo
        
        return self.backward_step[r][t][u]
        

    def gamma(self, r, t, u):
        if t in self.gamma_val[r] and u in self.gamma_val[r][t]:
            return self.gamma_val[r][t][u]

        if t not in self.gamma_val[r]:
            self.gamma_val[r][t] = {}

        val = self.alpha(r, t, u)*self.beta(r, t, u)

        den = 0
        for s in self.states:
            den += self.alpha(r, t, s)*self.beta(r, t, s)
        
        if val == 0:
            self.gamma_val[r][t][u] = 0
        else:    
            self.gamma_val[r][t][u] = (val/den)
        return self.gamma_val[r][t][u]

    def eta(self, r, t, u, v):
        if t in self.eta_val[r] and (u, v) in self.eta_val[r][t]:
            return self.eta_val[r][t][(u, v)]

        if t not in self.eta_val[r]:
            self.eta_val[r][t] = {}

        val = self.alpha(r, t, u)*self.delta[u][self.R[r][t+1]][v]*self.beta(r, t+1, v)

        den = 0
        for s in self.states:
            for s_ in self.states:
                den += self.alpha(r, t, s)*self.delta[s][self.R[r][t+1]][s_]*self.beta(r, t, s_)
        
        if val == 0:
            self.eta_val[r][t][(u, v)] = 0
        else:
            self.eta_val[r][t][(u, v)] = (val/den)
        return self.eta_val[r][t][(u, v)]