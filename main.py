import func
import classes
import numpy as np

initState = np.array([[1,2,3],[4,8,0],[7,6,5]])
goalState = np.array([[1,2,3],[4,5,6],[7,8,0]])

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
        break
    elif(userInput == "2"):
        # A* with the Misplaced Tile heuristic
        break
    elif(userInput == "3"):
        func.AStarEuclidean(puzzle)
        break
    else:
        print("Invalid choice. Please choose from the options prompted")