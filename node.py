class node:
    def __init__(self,value):
        self.pool = []
        for x in range(value):
            self.pool.append(x)
        self.state = (None)
        
    