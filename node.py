class node:
    def __init__(self,pool,state):
        #list of features
        self.pool = pool
        #tuple of the current state of the node
        self.state = state
        #int of the nodes accuracy
        self.acc=0
    