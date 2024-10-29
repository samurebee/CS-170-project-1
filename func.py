def moveZeroUp(z,s):
        if(z[0][0] != 0):
            new_s = s
            valueToSwitch = s[z[0][0] - 1][z[0][1]]
            new_s[z[0][0] - 1][z[0][1]] = 0
            new_s[z[0][0]][z[0][1]] = valueToSwitch
            return new_s
        else:
            print("Can not move up")
            return s

def moveZeroDown(z,s):
    if(z[0][0] != 2):
        new_s = s
        valueToSwitch = s[z[0][0] + 1][z[0][1]]
        new_s[z[0][0] + 1][z[0][1]] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        print("Can not move down")
        return s

def moveZeroLeft(z,s):
    if(z[0][1] != 0):
        new_s = s
        valueToSwitch = s[z[0][0]][z[0][1] - 1]
        new_s[z[0][0]][z[0][1] - 1] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        print("Can not move left")
        return s

def moveZeroRight(z,s):
    if(z[0][1] != 2):
        new_s = s
        valueToSwitch = s[z[0][0]][z[0][1] + 1]
        new_s[z[0][0]][z[0][1] + 1] = 0
        new_s[z[0][0]][z[0][1]] = valueToSwitch
        return new_s
    else:
        print("Can not move right")
        return s
