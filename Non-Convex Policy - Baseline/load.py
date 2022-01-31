import csv
import pickle
from actions import Actions

fl = open('grid-7-t1_Processed.csv')
csvreader = csv.reader(fl)

actions = Actions()
sn = {}
for row in csvreader:
    a_pos = (int(row[0]), int(row[1]))
    b_pos = (int(row[2]), int(row[3]))
    picked = False
    if(row[4].strip() == '1'):
        picked = True
    wrapped = False
    if(row[6].strip() == '1'):
        picked = True
    type = 'p'
    if(row[5].strip() == '1'):
        type = 'r'

    state = (a_pos, b_pos, picked, wrapped, type)
    action = actions.numToAction(row[7].strip())

    cost = float(row[8])
    if cost != 0:
        sn[(state, action)] = float(row[8])
    
print(sn)
file_to_write = open("state_action_NSE", "wb")
pickle.dump(sn, file_to_write)