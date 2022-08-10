import sys 
from actions import Actions
from misc import save

act = Actions()

action_map = {'0':act.up, '1':act.down, '2':act.left, '3':act.right, '4':act.pick_up, '5':act.wrap}

with open(sys.argv[1]) as file:
    pol = {}
    for line in file:
        end_tup = line.find(')')
        tup = line[1:end_tup]
        tup = tuple(i.strip() for i in tup.split(","))
        ag_loc = (int(tup[1]), int(tup[0]))
        box_loc = (int(tup[3]), int(tup[2]))
        picked = False
        if tup[4] == '1':
            picked = True
        wrapped = False
        if tup[6] == '1':
            wrapped = True
        car = 'p'
        if tup[5] == '1':
            car = 'r'
        st = (ag_loc, box_loc, picked, wrapped, car)
        pol[st] = {}
        for a in act.all_actions:
            pol[st][a] = 0
        pol[st][action_map[line[-4]]] = 1
    end_st = [((7, 14), (7, 14), True, False, 'p'), ((7, 14), (7, 14), True, True, 'p')]
    for e in end_st:
        pol[e] = {}
        for a in act.all_actions:
            pol[e][a] = 0
        pol[e][act.up] = 1
for s in pol:
    print(s)
    print(pol[s])
save("grid-15-0-learned.pkl", pol)