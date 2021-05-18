from node import *
from evaluate import *

class greedy:
    def __init__(self,node):
        self.frontier = {None}
        self.explored = {None}
        self.current_max = 0

    def accCheck(self,check):
        if self.current_max < check:
            self.current_max = check
            return False #no reduction found continue search
        else:
            return True #found reduction
    def childCheck(self,state):
        if state in self.explored:
            return True
        else:
            return False
