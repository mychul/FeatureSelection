from node import *
from validation import *
import random
#takes a list of node objects, evaluates them, returns the most accurate node with its score as a tuple
class evaluate:
    def __init__(self):
        self.evaluated = []

    def valuation(self,frontier,valid):
        self.evaluated.clear()
        for x in frontier:
            acc= valid.validate(x)
            self.evaluated.append((acc,x))
            #trace output
        for y in self.evaluated:
            print("Using feature(s) " + str(list(y[1])) + " accuracy is "+ str(y[0]))
        return max(self.evaluated)

