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

def get_states(state):
    newStates = []
    z = np.where(state == 0)

    for move in [moveZeroUp,moveZeroDown,moveZeroLeft,moveZeroRight]:
        currState = move(z,state)
        if currState is not None:
            newStates.append(currState)
    return newStates

def populate():
    print("Enter your 3 by 3 puzzle, type in \"0\" to represent the blank")
    row1 = input("Enter the first row, use a space between each number: ")
    row2 = input("Enter the second row, use a space between each number: ")
    row3 = input("Enter the third row, use a space between each number: ")
    intRow1 = [int(s) for s in re.findall(r'\d+', row1)] 
    intRow2 = [int(s) for s in re.findall(r'\d+', row2)] 
    intRow3 = [int(s) for s in re.findall(r'\d+', row3)] 
    initialState = np.array([intRow1, intRow2, intRow3])
    return initialState
            

def search(goalState,state):
    visited = set()




    

