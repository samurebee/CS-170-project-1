import numpy as np
import heapq
import re
import classes

def isValidInput(numbers): #checks if input has 1 of each # from 0-8
    return sorted(numbers) == list(range(9))

def getRowInput(row_num):
    while True:
        try:
            row = input(f"Enter row {row_num} (space-separated numbers from 0 to 8): ")
            
            # Extract numbers using regex
            numbers = [int(s) for s in re.findall(r'\d+', row)]
            
            # Validate that the row contains exactly 3 numbers between 0 and 8
            if len(numbers) != 3 or not all(0 <= n <= 8 for n in numbers):
                raise ValueError("Each row must contain exactly 3 numbers between 0 and 8.")
            
            return numbers  # Return the valid row
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def populate():
    
    print("Enter your 3 by 3 puzzle, type in \"0\" to represent the blank")
    while True:
        row1 = getRowInput(1)
        row2 = getRowInput(2)
        row3 = getRowInput(3)

        if isValidInput(row1+row2+row3):
            break  # Exit the loop if input is valid
        else:
            print("Invalid puzzle! Make sure you use all numbers from 0-8 with no repetition")

    initialState = np.array([row1, row2, row3])
    return initialState
         
def misplaced_tile_heuristic(state, goal_state):
    misplaced_count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced_count += 1
    return misplaced_count

def calculateEuclideanHeuristicCost(state, goalState):
        cost = 0
        length = len(state)
        for row in range(0,length):
            for column in range(0,length):
                if state[row][column] != goalState[row][column]:
                    goalIndex = np.argwhere(goalState == state[row][column])
                    cost += ((goalIndex[0][0] - row) ** 2 + (goalIndex[0][1] - column) ** 2) ** 0.5
        return cost

def checkIfStatesAreIdentical(state1, state2):
    length = len(state1)
    for row in range(0,3):
            for column in range(0,3): 
                if (state1[row][column] != state2[row][column]):
                    return False
    return True

def getStates(puzzle, explored, frontier):
    newStates = []

    for move in [puzzle.moveZeroUp,puzzle.moveZeroDown,puzzle.moveZeroLeft,puzzle.moveZeroRight]:
        z = np.argwhere(puzzle.currState == 0)
        newState = move(z,puzzle.currState)
        if ((checkIfStatesAreIdentical(puzzle.currState,newState)) == False):
            flag = False
            if (len(explored) != 0):
                for states in explored:
                    if ((checkIfStatesAreIdentical(newState,states)) == True):
                        flag = True
                        break
            for states in frontier:
                if(flag == True):
                    break
                if ((checkIfStatesAreIdentical(newState,states[0])) == True):
                    flag = True
                    break
            if (flag == False):
                newStates.append(newState)
    return newStates

def sortFrontier(frontier, stateToSort, fCost, gCost, hCost):
    count = 0
    flag = 0
    if (len(frontier) != 0):
        for state in frontier:
            if (state[1] > fCost):
                frontier.insert(count, [stateToSort, fCost, gCost, hCost])
                flag = 1
                break
            count += 1
    if(flag == 0):
        frontier.append([stateToSort, fCost, gCost, hCost])
    return frontier 

def algorithmChoice(a, currState, goalState):
    if(a == 1):
        return 0
    elif(a == 2):
        return misplaced_tile_heuristic(currState, goalState)
    else:
        return calculateEuclideanHeuristicCost(currState, goalState)

def search(puzzle, algorithm):
    
    initialStateCost = algorithmChoice(algorithm, puzzle.initialState, puzzle.goalState)
    frontier = [[puzzle.initialState, initialStateCost, 0, initialStateCost]]
    maxFrontier = 1
    explored = []
    gCost = 0
    print("Expanding State")
    puzzle.printState(puzzle.currState)
    expanded = 0
    while(1):
        if(len(frontier) == 0):
            print("Failed")
            return -1
        if((checkIfStatesAreIdentical(puzzle.currState,puzzle.goalState)) == True):
            explored.append(puzzle.currState)
            print("Goal!!!")

            print("To solve this problem the search algorithm expanded a total of %d nodes." % (expanded))
            print("The maximum number of nodes in the queue at one time: %d." % (maxFrontier))
            print("The depth of the goal node was %d." % (frontier[0][2]))
            frontier.clear()
            break
        if (gCost != 0):
            if(algorithm == 3):
                print("The best state to expand with g(n) = %d and h(n) = %f is" % (frontier[0][2], frontier[0][3]))
            else:
                print("The best state to expand with g(n) = %d and h(n) = %d is" % (frontier[0][2], frontier[0][3]))
            puzzle.printState(frontier[0][0])
            print("Expanding this Node")
        gCost = frontier[0][2] + 1
        explored.append(puzzle.currState)
        frontier.pop(0)
        expanded += 1
        newStates = getStates(puzzle, explored, frontier)
        if (len(newStates) != 0):
            for state in newStates:
                hCost = algorithmChoice(algorithm, state, puzzle.goalState)
                fCost = hCost + gCost
                sortFrontier(frontier, state, fCost, gCost, hCost)
                if(len(frontier) > maxFrontier):
                    maxFrontier = len(frontier)
        if(len(frontier) != 0):
            puzzle.currState = frontier[0][0]






    

