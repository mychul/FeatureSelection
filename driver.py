from node import *
from forward import *
from backward import *

print("Welcome to 861126014 (Michael Chiang) & 861199635 (Tinh La) group's Feature Selection Algorithm.\n")
numFeatures = input("Please enter total number of features: ")
#numFeatures = 7 #debug purposes
initialPool=[]
for x in range(int(numFeatures)):
    initialPool.append(x)
start = node(initialPool,None, numFeatures)
print("\n") #Empty line
print("Type the number of the algorithm you want to run: ")
print("(1) - Forward Selection\n(2) - Backward Elimination\n")
algoChoice = input("Choice: ")
algoChoice = int(algoChoice)
#algoChoice = 1 #debug purposes
initial_acc = random.randint(0,100)
print("Using no features and random evaluation, accuracy is " + str(initial_acc))
if algoChoice == 1:
    #forward selection
    forward = forward(start,initial_acc)
    forward.start()
    pass
elif algoChoice == 2:
    #backward elimination
    back = backward(start,initial_acc)
    back.start()
else:
    print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")