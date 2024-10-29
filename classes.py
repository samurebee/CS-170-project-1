import numpy as np

class Problem:

    def __init__(self, initialState = np.array([[1,2,3], [4,8,0], [7,6,5]])):
        self.initialState = initialState
        self.goalState = np.array([[1,2,3], [4,5,6], [7,8,0]])
    
    def moveZeroUp(z,s):
        if(z[0][0] != 0):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0] - 1][z[0][1]]
            new_s[z[0][0] - 1][z[0][1]] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return None

    def moveZeroDown(z,s):
        if(z[0][0] != 2):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0] + 1][z[0][1]]
            new_s[z[0][0] + 1][z[0][1]] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return None

    def moveZeroLeft(z,s):
        if(z[0][1] != 0):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0]][z[0][1] - 1]
            new_s[z[0][0]][z[0][1] - 1] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return None

    def moveZeroRight(z,s):
        if(z[0][1] != 2):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0]][z[0][1] + 1]
            new_s[z[0][0]][z[0][1] + 1] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return None

    def printState(state):
        print(state[0][0] , state[0][1], state[0][2], sep = " ")
        print(state[1][0] , state[1][1], state[1][2], sep = " ")
        print(state[2][0] , state[2][1], state[2][2], sep = " ")
        print("\n")
class Node:
    def __init__(self, value, hCost = 0, gCost = 0, fCost = 0):
        self.value = value
        self.children = []
        self.hCost = hCost
        self.gCost = gCost
        self.fCost = fCost 
    def addChild(self, child):
        self.children.append(child)
    def returnValue(self):
        return self.value
    def returnhCost(self):
        return self.hCost
    def returngCost(self):
        return self.gCost
    def returnfCost(self):
        return self.fCost
    

class Tree:
    def __init__(self,root):
        self.root = root
    def addNode(self, newNode, parent=None):
        parent.addChild(newNode)