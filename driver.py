from node import *
from forward import *
from backward import *

print("Welcome to 861126014 (Michael Chiang) & 861199635 (Tinh La) group's Feature Selection Algorithm.\n")
numFeatures = input("Please enter total number of features: ")
start = node(numFeatures,None)
print("\n") #Empty line
print("Type the number of the algorithm you want to run: ")
print("(1) - Forward Selection\n(2) - Backward Elimination\n")
algoChoice = input("Choice: ")
algoChoice = int(algoChoice)

if algoChoice == 1:
    #forward selection
    pass
elif algoChoice == 2:
    #backward elimination
    pass
else:
    print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
