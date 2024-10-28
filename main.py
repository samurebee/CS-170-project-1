import numpy as np
import heapq

def problem():

    initial_state = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]

    goal_state = [[1, 2, 3],  [4, 5, 6], [7, 8, 0]]

    zero_index = np.argwhere(initial_state == 0)
    zero_position = tuple(zero_index[0])

    def calculate_gn(parent_gn):
        return parent_gn + 1

    def calculate_fn(gn, hn):
        return gn + hn

    def move_zero_up(s, z):
        if(z[0][0] != 0):
            value_to_switch = s[z[0][0] - 1][z[0][1]]
            s[z[0][0] - 1][z[0][1]] = 0
            s[z[0][0]][z[0][1]] = value_to_switch
        else:
            print("Cannot move up")

    def move_zero_down(s, z):
        if(z[0][0] != 2):
            value_to_switch = s[z[0][0] + 1][z[0][1]]
            s[z[0][0] + 1][z[0][1]] = 0
            s[z[0][0]][z[0][1]] = value_to_switch
        else:
            print("Cannot move down")

    def move_zero_left(s, z):
        if(z[0][1] != 0):
            value_to_switch = s[z[0][0]][z[0][1] - 1]
            s[z[0][0]][z[0][1] - 1] = 0
            s[z[0][0]][z[0][1]] = value_to_switch
        else:
            print("Cannot move left")

    def move_zero_right(s, z):
        if(z[0][1] != 2):
            value_to_switch = s[z[0][0]][z[0][1] + 1]
            s[z[0][0]][z[0][1] + 1] = 0
            s[z[0][0]][z[0][1]] = value_to_switch
        else:
            print("Cannot move right")