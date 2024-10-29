import numpy as np
import heapq

def moveZeroUp(z,s):
    if(z[0][0] != 0):
        new_s = s
        valueToSwitch = s[z[0][0] - 1][z[0][1]]
        new_s[z[0][0] - 1][z[0][1]] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        print("Can not move up")
        return None

def moveZeroDown(z,s):
    if(z[0][0] != 2):
        new_s = s
        valueToSwitch = s[z[0][0] + 1][z[0][1]]
        new_s[z[0][0] + 1][z[0][1]] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        print("Can not move down")
        return None

def moveZeroLeft(z,s):
    if(z[0][1] != 0):
        new_s = s
        valueToSwitch = s[z[0][0]][z[0][1] - 1]
        new_s[z[0][0]][z[0][1] - 1] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        return None

def moveZeroRight(z,s):
    if(z[0][1] != 2):
        new_s = s
        valueToSwitch = s[z[0][0]][z[0][1] + 1]
        new_s[z[0][0]][z[0][1] + 1] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        return None
    

def getZeroPosition(state):
    pos = np.where(state == 0)
    return (pos[0][0], pos[1][0])  # Return as (row, col)

def get_states(state):
    newStates = []
    z = getZeroPosition(state)

    for move in [moveZeroUp,moveZeroDown,moveZeroLeft,moveZeroRight]:
        currState = move(z,state)
        if currState is not None:
            newStates.append(currState)
    return newStates





def ucs(goalState,state):
    visited = set()




    

