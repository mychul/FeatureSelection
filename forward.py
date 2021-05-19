from greedy import *

class forward(greedy):
    def __init__(self,node):
        super().__init__(node)
        best_accuracy = -1
        cur_accuracy = 0
        cur_node = node
        #assign = evaluate([cur_node])

    def start(self):
        #self.
        while not self.accCheck():
            if not self.childCheck(self.cur_node.state):
                self.spawnChild(self.cur_node.state,)
        #pass
    def spawnChild(self,state,acc):
        pass