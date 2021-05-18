class node:
    def __init__(self,value,state):
        self.pool = []
        for x in range(value):
            self.pool.append(x)
        self.state = (state)
        
    