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

                

def get_states(state):
    newStates = []
    z = np.where(state == 0)

    for move in [classes.moveZeroUp,classes.moveZeroDown,classes.moveZeroLeft,classes.moveZeroRight]:
        currState = move(z,state)
        if currState is not None:
            newStates.append(currState)
    return newStates

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

def sortFrontier(frontier, stateToSort, fCost):
    count = 0
    if (len(frontier) != 0):
        for state in frontier:
            if (state[1] > fCost):
                frontier.insert(count, [stateToSort, fCost])
                break
            count += 1
        return frontier
    else:
        frontier.append([stateToSort, fCost])    

def AStarEuclidean(puzzle):
    initialStateCost = calculateEuclideanHeuristicCost(puzzle.initialState, puzzle.goalState)
    nodeState = classes.Node(puzzle.initialState, initialStateCost, 0, initialStateCost)
    parentNode = nodeState
    # puzzleTree = Tree(puzzle.initialState) 
    frontier = [[puzzle.initialState, initialStateCost]]
    explored = []
    gCost = 1
    print("Expanding State")
    puzzle.printState(puzzle.currState)
    while(1):
        if(len(frontier) == 0):
            print("Failed")
            return -1
        if((checkIfStatesAreIdentical(puzzle.currState,puzzle.goalState)) == True):
            if((checkIfStatesAreIdentical(puzzle.currState, puzzle.initialState)) == False):
                hCost = calculateEuclideanHeuristicCost(puzzle.currState,puzzle.goalState)
                fCost = hCost + gCost
                newNode = classes.Node(puzzle.currState, hCost,gCost, fCost)
            frontier.clear()
            explored.append(puzzle.currState)
            print("Goal!!!")
            break
        if (gCost != 1):
            print("The best state to expand with g(n) = %d and h(n) = %f is" % (newNode.gCost, newNode.hCost))
            puzzle.printState(frontier[0][0])
            print("Expanding this Node")
        explored.append(puzzle.currState)
        frontier.pop(0)
        newStates = getStates(puzzle, explored, frontier)
        if (len(newStates) != 0):
            for state in newStates:
                fCost = 0
                hCost = calculateEuclideanHeuristicCost(state, puzzle.goalState)
                fCost = hCost + gCost
                newNode = classes.Node(state, hCost, gCost, fCost)
                # puzzleTree.addNode(newNode, parentNode)
                sortFrontier(frontier, state, fCost)
        gCost += 1
        # parentNode = puzzle.currState
        puzzle.currState = frontier[0][0]
        while(1):
            userInput = input("Input: ")
            if(userInput == "1"):
                break      

def ucs(puzzle):
    # Priority queue: stores (gCost, state (as a tuple), path from start to current state)
    frontier = []
    explored = []  # List to keep track of explored states

    # Convert the initial state to a tuple and push it onto the queue with gCost = 0
    initial_state_tuple = tuple(puzzle.initialState.flatten())
    heapq.heappush(frontier, (0, initial_state_tuple, [puzzle.initialState]))

    print("Starting Uniform Cost Search...")

    while frontier:
        # Get the state with the lowest gCost
        current_cost, current_state_tuple, path = heapq.heappop(frontier)
        current_state = np.array(current_state_tuple).reshape(puzzle.initialState.shape)

        print(f"\nExpanding Node with gCost={current_cost}:")
        puzzle.printState(current_state)  # Print the current state

        # If the goal state is reached, print the final path and exit
        if np.array_equal(current_state, puzzle.goalState):
            print("\nGoal reached! Solution path:")
            for step in path:
                puzzle.printState(step)
                print("-----")
            print(f"Total cost: {current_cost}")
            return

        # Mark the current state as explored
        explored.append(current_state_tuple)

        # Generate all possible new states from the current state
        zero_pos = np.argwhere(current_state == 0)  # Position of 0 (blank tile)
        new_states = [
            puzzle.moveZeroUp(zero_pos, current_state),
            puzzle.moveZeroDown(zero_pos, current_state),
            puzzle.moveZeroLeft(zero_pos, current_state),
            puzzle.moveZeroRight(zero_pos, current_state)
        ]

        for state in new_states:
            if state is not None:
                # Convert state to a tuple for comparability
                state_tuple = tuple(state.flatten())

                # Check if the state is already explored
                if state_tuple in explored:
                    continue

                # Add the new state to the frontier with updated gCost
                new_cost = current_cost + 1  # Increment path cost
                new_path = path + [state]
                heapq.heappush(frontier, (new_cost, state_tuple, new_path))

    print("No solution found.")





    

