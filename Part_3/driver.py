from node import *
from forward import *
from backward import *
from classifier import *
from validation import *

invalidChoice = False

def getAlgoChoice():
    print("Type the number of the algorithm you want to run: ")
    print("(1) - Forward Selection\n(2) - Backward Elimination\n")
    algoChoice = input("Choice: ")
    if algoChoice.isdigit():
        algoChoice = int(algoChoice)
    else:
        invalidChoice = True
    return algoChoice


print("Welcome to 861126014 (Michael Chiang) & 861199635 (Tinh La) group's Feature Selection Algorithm.\n")
print("(1) - Small Data\n(2) - Large Data\n(3) - Personal Small\n(4) - Personal Large\n")
dataSetChoice = input("Choice: ")
if dataSetChoice.isdigit():
    dataSetChoice = int(dataSetChoice)
    
    classy = classifier()
    classy.train(dataSetChoice)
    valid = validator(classy)
    initialPool=[]
    for x in range(classy.size):
        initialPool.append(x)
    start = node(initialPool,None,classy.size)   
else:
    invalidChoice = True

#initial_acc = random.randint(0,100)
if not invalidChoice:
    algoChoice = -1
    invalidChoice = False
    if dataSetChoice == 1:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            
            #forward selection
            forward = forward(start,classy.defaultRate,valid)
            forward.start()
            
        elif algoChoice == 2:
            #backward elimination
            backward = backward(start,classy.defaultRate,valid)
            backward.start()
            
        else:
            invalidChoice = True
    elif dataSetChoice == 2:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            #forward selection
            forward = forward(start,classy.defaultRate,valid)
            forward.start()
            
        elif algoChoice == 2:
            #backward elimination
            backward = backward(start,classy.defaultRate,valid)
            backward.start()
        else:
            invalidChoice = True
    elif dataSetChoice == 3:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            #forward selection
            forward = forward(start,classy.defaultRate,valid)
            forward.start()
               
        elif algoChoice == 2:
            #backward elimination
            backward = backward(start,classy.defaultRate,valid)
            backward.start()
        else:
            invalidChoice = True
    elif dataSetChoice == 4:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            #forward selection
            forward = forward(start,classy.defaultRate,valid)
            forward.start()
               
        elif algoChoice == 2:
            #backward elimination
            backward = backward(start,classy.defaultRate,valid)
            backward.start()
        else:
            invalidChoice = True
    else:
        invalidChoice = True
else:
    print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
    # print("Using no features and random evaluation, accuracy is " + str(initial_acc))