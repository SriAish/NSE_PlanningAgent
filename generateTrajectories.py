from boxPushingEnv import BoxPushing
from randomAgent import RandomAgent
from VIAgent import VIPolicy
import csv
import copy
import numpy as np

env = BoxPushing(15, [0, 0], [7, 14], [7, 0])

def checkDamage(t):
    rug = np.zeros((3, 7))
    st = (6, 4)
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

    return (np.count_nonzero(rug)/21) * 100

def generate_trajectory(agent):
    env = BoxPushing()
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

        s, c, done = env.getNextState(a)

        # print(s, a, done)        
    # env.display()
    return t, ac

def generate_n_tajectories(n, agent):
    with open('trajectories.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["trajectory", "Type", "Size"])
        i = 0
        while i < 50:
            t, ac = generate_trajectory(agent)
            c = "severe"
            damage = checkDamage(t)

            if damage < 1:
                continue
            if damage < 25:
                c = "mild"

            i += 1

            csvwriter.writerow([t, c, ac])
            print(t, damage, ac)

if __name__ == '__main__':
    # agent = RandomAgent([7, 14])
    agent = VIPolicy("policy/VIPolicy.pkl")
    generate_n_tajectories(50, agent)
    # generate_trajectory(agent)