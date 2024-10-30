import numpy as np

class Problem:

    def __init__(self, initialState = np.array([[1,2,3], [4,8,0], [7,6,5]])):
        self.initialState = initialState
        self.currState = initialState
        self.goalState = np.array([[1,2,3], [4,5,6], [7,8,0]])
    
    def moveZeroUp(self,z,s):
        if(z[0][0] != 0):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0] - 1][z[0][1]]
            new_s[z[0][0] - 1][z[0][1]] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return s

    def moveZeroDown(self,z,s):
        if(z[0][0] != 2):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0] + 1][z[0][1]]
            new_s[z[0][0] + 1][z[0][1]] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return s

    def moveZeroLeft(self,z,s):
        if(z[0][1] != 0):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0]][z[0][1] - 1]
            new_s[z[0][0]][z[0][1] - 1] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return s

    def moveZeroRight(self,z,s):
        if(z[0][1] != 2):
            new_s = np.copy(s)
            valueToSwitch = s[z[0][0]][z[0][1] + 1]
            new_s[z[0][0]][z[0][1] + 1] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            return s

    def printState(self,state):
        print(state[0][0] , state[0][1], state[0][2], sep = " ")
        print(state[1][0] , state[1][1], state[1][2], sep = " ")
        print(state[2][0] , state[2][1], state[2][2], sep = " ")
        