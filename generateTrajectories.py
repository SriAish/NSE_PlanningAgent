from boxPushingEnv import BoxPushing
from randomAgent import RandomAgent
from VIAgent import VIPolicy
import csv
import copy
import numpy as np

def checkDamage(t, st=[6, 4]):
    rug = np.zeros((3, 3))
    n = 0
    ind = 0
    for i in t:
        # print("string: ", i)
        if type(i) is str:
            continue
        if i[3] == 'r':
            rug[i[0][0] - st[0], i[0][1] - st[1]] = 1
        ind += 1
    
    # print(rug)
    
    # print(np.count_nonzero(rug))

    return (np.count_nonzero(rug)/9) * 100

def generate_trajectory(agent):
    env = env = BoxPushing(7, [0, 0], [3, 6], rug_width=3, rug_height=3, rug_start=[2, 2], locations=[[3, 0], [1, 2], [0, 3], [6, 3], [5, 4]])
    done = False
    t = []
    ac = 0
    while not done and ac < 1000:
        s = env.getState()
        a = agent.getAction(s)
        # print(ac, s)
        # env.display()
    
        t = t + [copy.deepcopy(s), a]

        ac += 1

        s, _, done = env.getNextState(a)

        # print(s, a, done)        
    # env.display()
    return t, ac

def generate_n_tajectories(n, agent):
    with open('trajectories_7_7.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["trajectory", "Type", "Size"])
        i = 0
        while i < 50:
            t, ac = generate_trajectory(agent)
            c = "severe"
            damage = checkDamage(t, [2, 2])

            if damage < 1:
                continue
            if damage < 25:
                c = "mild"

            i += 1

            csvwriter.writerow([t, c, ac])
            print(t, damage, ac)

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    agent = VIPolicy("policy/VIPolicy_7_7_2.pkl")
    generate_n_tajectories(50, agent)
    # generate_trajectory(agent)