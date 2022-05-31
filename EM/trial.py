from FB import FB

R = [['a', 'a', 'b', 1], ['b', 'a', 'b', 1]]

delta = {}
delta['0'] = {}
delta['1'] = {}
delta['2'] = {}
delta['#'] = {}

delta['0']['a'] = {}
delta['0']['b'] = {}
delta['1']['a'] = {}
delta['1']['b'] = {}
delta['2']['a'] = {}
delta['2']['b'] = {}
delta['#']['a'] = {}
delta['#']['b'] = {}

delta['0']['a']['1'] = 1
delta['0']['a']['2'] = 0
delta['0']['b']['1'] = 0
delta['0']['b']['2'] = 1

delta['1']['a']['1'] = 1
delta['1']['a']['2'] = 0
delta['1']['a']['#'] = 0
delta['1']['b']['1'] = 0
delta['1']['b']['2'] = 0
delta['1']['b']['#'] = 1

delta['2']['a']['1'] = 0.5
delta['2']['a']['2'] = 0.5
delta['2']['a']['#'] = 0
delta['2']['b']['1'] = 0
delta['2']['b']['2'] = 0
delta['2']['b']['#'] = 1

omega = {}
omega['1'] = {}
omega['2'] = {}
omega['1']['a'] = {}
omega['1']['b'] = {}
omega['2']['a'] = {}
omega['2']['b'] = {}

omega['1']['a'][0] = 0
omega['1']['a'][1] = 0
omega['1']['a'][2] = 1
omega['1']['b'][0] = 0
omega['1']['b'][1] = 1
omega['1']['b'][2] = 0

omega['2']['a'][0] = 0
omega['2']['a'][1] = 0
omega['2']['a'][2] = 1
omega['2']['b'][0] = 0
omega['2']['b'][1] = 1
omega['2']['b'][2] = 0

states = ['1', '2']

fb = FB(delta, omega, states, R)
tr = 0
ts = 0
st = '2'

# gamma = fb.alpha(tr, ts, st)*fb.beta(tr, ts, st)
# den = 0

# for s in states:
#     den += fb.alpha(tr, ts, s)*fb.beta(tr, ts, s)

pr = 0
for s in states:
    print("state: ", s)
    pr += fb.alpha(tr, len(R[tr]) - 3, s)*fb.beta(tr, len(R[tr]) - 3, s)

print(pr)

# print(gamma/den)
# print(fb.eta(tr, ts, st, st))