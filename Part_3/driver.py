from node import *
from forward import *
from backward import *

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
            #forward = forward(start,initial_acc)
            #forward.start()
            pass
        elif algoChoice == 2:
            #backward elimination
            #back = backward(start,initial_acc)
            #back.start()
            pass
        else:
            invalidChoice = True
    elif dataSetChoice == 2:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            #forward selection
            #forward = forward(start,initial_acc)
            #forward.start()
            pass
        elif algoChoice == 2:
            #backward elimination
            #back = backward(start,initial_acc)
            #back.start()
            pass
        else:
            invalidChoice = True
    elif dataSetChoice == 3:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            #forward selection
            #forward = forward(start,initial_acc)
            #forward.start()
            pass
        elif algoChoice == 2:
            #backward elimination
            #back = backward(start,initial_acc)
            #back.start()
            pass
        else:
            invalidChoice = True
    elif dataSetChoice == 4:
        algoChoice = getAlgoChoice()
        if algoChoice == 1:
            #forward selection
            #forward = forward(start,initial_acc)
            #forward.start()
            pass
        elif algoChoice == 2:
            #backward elimination
            #back = backward(start,initial_acc)
            #back.start()
            pass
        else:
            invalidChoice = True
    else:
        invalidChoice = True
else:
    print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
    # print("Using no features and random evaluation, accuracy is " + str(initial_acc))