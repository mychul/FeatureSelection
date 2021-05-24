from node import *
from evaluate import *
import itertools

class greedy:
    def __init__(self,node):
        self.cursor=node
        self.frontier = {None}
        self.explored = {}
        self.current_max = 0
        self.flag=False
        self.eval = evaluate()

    def accCheck(self,check):
        if self.current_max < check:
            self.current_max = check
            print("No reduction found, continuing...")
            return #no reduction found continue search
        else:
            print("Reduction Found")
            print("Finished Search! The best feature subset is "+ str(list(self.cursor.state)) +", which has an accuracy of " + str(self.cursor.acc))
            self.flag =True
            return #found reduction

    def childCheck(self,state):
        if state in self.explored:
            return True
        else:
            return False
    #adds the current node and its state(key) to the explored dict
    def updateExplored(self):
        self.explored[self.cursor.state]=self.cursor
        return
        

