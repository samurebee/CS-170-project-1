import func
import classes
import numpy as np


while(1):
    print("Welcome to CS170 8 puzzle solver.")
    userInput = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle: ") 
    if (userInput == "1"):
        puzzle = classes.Problem()
        break
    elif (userInput == "2"):
        puzzle = classes.Problem(func.populate())
        break
    else:
        print("Invalid choice. Please choose from the options prompted")
while(1):
    print("Enter your choice of algorithm")
    print("Type \"1\" for Uniform Cost Search.")
    print("Type \"2\" for A* with the Misplaced Tile heuristic.")
    print("Type \"3\" for A* with the Euclidean distance heuristic.")
    userInput = input()
    if(userInput == "1"):
        # Uniform Cost Search
        func.search(puzzle, 1)
        break
    elif(userInput == "2"):
        func.search(puzzle, 2)
        break
    elif(userInput == "3"):
        func.search(puzzle, 3)
        break
    else:
        print("Invalid choice. Please choose from the options prompted")