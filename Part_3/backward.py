from greedy import *

#pool is a little redundant in backward since we are removing an element from the state to generate the child
#the explored dictionary is also unneeded for a similar reason in conjunction with itertools combinations to generate children
class backward(greedy):
    def __init__(self,node,initial,valid):
        super().__init__(node)
        self.current_max= initial
        #set state to pool because backwards
        self.cursor.state=(self.cursor.pool)
        #give this node an acc
        #TODO
        valid.validate(self.cursor.state)

    
    def start(self):
        print ("Beginning Search: ")
        print("Using feature(s) " + str(self.cursor.state) + " accuracy is "+ str(self.cursor.acc))
        #check if no features is better
        if self.cursor.acc < self.current_max:
            print("Reduction Found")
            print("Finished Search! The best feature subset is nothing which has an accuracy of " + str(self.current_max))
            return
        else:
            self.current_max = self.cursor.acc
        #loop until reduction in acc or we have reached a state of 1
        while(not self.flag or len(self.cursor.state) == 1):
            self.spawnChild()
            #evaluates frontier finding best
            
            bestChild= self.eval.valuation(self.frontier,self.validator) #(acc,state)
            print("Best Feature set is " + str(list(bestChild[1])) + " with accuracy " + str(bestChild[0]))
            #check for reduction
            self.accCheck(bestChild[0])
            
            #if no reduction found
            if not self.flag:
                #set cursor to bestchild
                self.cursor = node(sorted(bestChild[1]),bestChild[1],0)
                self.cursor.acc = bestChild[0]
                self.frontier = (None)
                if len(bestChild[1]) == 1:
                    print("Finished Search due to end of expansion! The best feature subset is "+ str(list(self.cursor.state)) +", which has an accuracy of " + str(self.cursor.acc))
                    return
                
        return
        #spawns tuples of features that are the possible combinations based on the current state
        #unique to backward since we are removing one element from the full feature list
    def spawnChild(self):
        #print (self.cursor.state)
        #print (len(self.cursor.state))
        self.frontier = itertools.combinations(self.cursor.state,len(self.cursor.state)-1)
        #for x in self.frontier:
            #print (x)
        