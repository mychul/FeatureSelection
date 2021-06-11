from node import *
from forward import *
from backward import *

print("Welcome to 861126014 (Michael Chiang) & 861199635 (Tinh La) group's Feature Selection Algorithm.\n")
print("\n")
print("(1) - Small Data\n(2) - Large Data\n(3) - Personal Small\n(4) - Personal Large\n")
dataSetChoice = input("Choice: ")
dataSetChoice = int(dataSetChoice)
initial_acc = random.randint(0,100)
algoChoice = -1
if dataSetChoice == 1:
    print("Type the number of the algorithm you want to run: ")
    print("(1) - Forward Selection\n(2) - Backward Elimination\n")
    algoChoice = input("Choice: ")
    algoChoice = int(algoChoice)
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
        print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
elif dataSetChoice == 2:
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
        print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
elif dataSetChoice == 3:
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
        print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
elif dataSetChoice == 4:
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
        print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")
else:
    print("Invalid choice entered.  Please rereun the Feature Selection program and enter a valid choice.")

# print("Using no features and random evaluation, accuracy is " + str(initial_acc))