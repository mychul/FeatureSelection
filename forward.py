from greedy import *

class forward(greedy):
    def __init__(self,node,initial):
        super().__init__(node)
        self.current_max= initial
        #set state to pool because backwards
        self.cursor.state=()
        #give this node an acc
        self.cursor.acc= 1
       
        
        
        

    def start(self):
        print ("Beginning Search: ")
        #print("Using feature(s) " + str(self.cursor.state) + " accuracy is "+ str(self.cursor.acc))
        #check if no features is better
        if self.cursor.acc < self.current_max:
            print("Reduction Found")
            print("Finished Search! The best feature subset is nothing which has an accuracy of " + str(self.current_max))
            return
        else:
            self.current_max = self.cursor.acc
        #loop until reduction in acc or we have reached a state of 1
            while(not self.flag):
                for x in self.cursor.pool:
                    #temp = x
                    if not len(self.cursor.state) == 0:
                        for y in self.cursor.state: 
                            if x + 1 != y:
                                self.spawnChild(x+1)
                    else:
                        self.spawnChild(x+1)
                #evaluates frontier finding best
                
                bestChild= self.eval.randoList(self.frontier) #(acc,state)
                print("Best Feature set is " + str(list(bestChild[1])) + " with accuracy " + str(bestChild[0]))
                #check for reduction
                self.accCheck(bestChild[0])
                
                #if no reduction found
                if not self.flag:
                    #set cursor to bestchild
                    self.cursor = node(self.cursor.pool,bestChild[1], self.cursor.num)
                    self.cursor.acc = bestChild[0]
                    self.frontier.clear()
                    if len(bestChild[1]) == self.cursor.num:
                        print("Finished Search due to end of expansion! The best feature subset is "+ str(list(self.cursor.state)) +", which has an accuracy of " + str(self.cursor.acc))
                        return
                        
        #spawns tuples of features that are the possible combinations based on the current state
        #unique to backward since we are removing one element from the full feature list
        #while not self.accCheck():
            #if not self.childCheck(self.cur_node.state):
                #self.spawnChild(self.cur_node.state,)
        return
    def spawnChild(self,x):
        if not x in self.cursor.state:
            temp_list = []
            temp_list.append(x)
            temp_list = self.cursor.state +tuple(temp_list)
            temp_list = sorted(temp_list)
            self.frontier.add(tuple(temp_list))
        #print(temp_list)
        #exit(0)
        #self.frontier = itertools.combinations(self.cursor.state,len(self.cursor.state)-1)  # NOTE: DOES NOT WORK
       