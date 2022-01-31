import csv
import pickle
from actions import Actions
import sys
from misc import BoxPushingConstants

# fl = open('grid-7-t1_Processed.csv')
# csvreader = csv.reader(fl)

# actions = Actions()
# sn = {}
# for row in csvreader:
#     a_pos = (int(row[0]), int(row[1]))
#     b_pos = (int(row[2]), int(row[3]))
#     picked = False
#     if(row[4].strip() == '1'):
#         picked = True
#     wrapped = False
#     if(row[6].strip() == '1'):
#         picked = True
#     type = 'p'
#     if(row[5].strip() == '1'):
#         type = 'r'

#     state = (a_pos, b_pos, picked, wrapped, type)
#     action = actions.numToAction(row[7].strip())

#     cost = float(row[8])
#     if cost != 0:
#         sn[(state, action)] = float(row[8])
    
# print(sn)
# file_to_write = open("state_action_NSE", "wb")
# pickle.dump(sn, file_to_write)

def load(name):
    file_to_read = open(name, "rb")
    return pickle.load(file_to_read)

sn = load("state_action_NSE")

g_pos = (int(sys.argv[6]), int(sys.argv[7]))
e_state = [(g_pos, g_pos, True, False, 'p'), (g_pos, g_pos, True, True, 'p')]
BP = BoxPushingConstants(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), (int(sys.argv[4]), int(sys.argv[5])), e_state)
for s in BP.states:
    actions = BP.getValidActions(s)
    nse = 0
    for a in actions:
        if (s,a) in sn:
            print("in")