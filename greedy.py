from node import *
from evaluate import *

class greedy:
    def __init__(self,node):
        self.frontier = {None}
        self.explored = {None}
        self.current_max = 0
