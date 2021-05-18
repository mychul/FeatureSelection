from node import *
from forward import *
from backward import *

print("Welcome to 861126014 (Michael Chiang) & 861199635 (Tinh La) group's Feature Selection Algorithm.\n")
numFeatures = input("Please enter total number of features: ")
print("\n") #Empty line
print("Type the number of the algorithm you want to run: ")
print("(1) - Forward Selection\n(2) - Backward Elimination\n")
algoChoice = input("Choice: ")
#run algo