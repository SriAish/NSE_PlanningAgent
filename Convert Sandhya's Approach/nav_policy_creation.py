import sys 
from nav_actions import Actions
from misc import save

act = Actions()

action_map = {'0':act.left_slow, '1':act.left_fast, '2':act.right_slow, '3':act.right_fast, '4':act.up_slow, '5':act.up_fast, '6':act.down_slow, '7':act.down_fast}

with open(sys.argv[1]) as file:
    pol = {}
    for line in file:
        end_tup = line.find(')')
        tup = line[1:end_tup]
        tup = tuple(i.strip() for i in tup.split(","))
        ag_loc = (int(tup[1]), int(tup[0]))
        speed = 'slow'
        if tup[2] == '2':
            speed = 'fast'
        ped = False
        pud = False
        if tup[3] == '1':
            ped = True
            pud = True
        if tup[4] == '1':
            pud = True
        st = (ag_loc, speed, ped, pud)
        pol[st] = {}
        for a in act.all_actions:
            pol[st][a] = 0
        # print(line)
        # print("5:", line[-5],"3:",  line[-3],"2:",  line[-2],"1:",  line[-1])
        pol[st][action_map[line[-4]]] = 1
    end_st = [((14, 14), 'fast', False, False), ((0, 3), 'slow', False, False)]
    for e in end_st:
        pol[e] = {}
        for a in act.all_actions:
            pol[e][a] = 0
        pol[e][act.up_fast] = 1
for s in pol:
    print(s)
    print(pol[s])
save("grid-3-t1-nav_Policy-15-ler.pkl", pol)