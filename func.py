import numpy as np
import heapq
import re
import classes

def is_valid_input(numbers): #checks if input has 1 of each # from 0-8
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

        if is_valid_input(row1+row2+row3):
            break  # Exit the loop if input is valid
        else:
            print("Invalid puzzle! Make sure you use all numbers from 0-8 with no repetition")

    initialState = np.array([row1, row2, row3])
    return initialState
         
        
            

def search(goalState,state):
    visited = set()




    

