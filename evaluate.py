from node import *
import random
#takes a list of node objects, evaluates them, returns the most accurate node with its score as a tuple
class evaluate:
    def __init__(self,frontier):
        self.frontier = frontier
        self.evaluated = []

    def rando(self):
        for x in self.frontier:
            ran = random.randint(0,100)
            self.evaluated.append((ran,x))
        return max(self.evaluated)
