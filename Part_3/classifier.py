import math
import re
import copy
from statistics import *
class classifier:
    def __init__(self):
        self.dataset = []
        self.book = []
        self.defaultRate =0
        self.size=0
        self.tsize=0
    def train(self,option):
        #reading data
        if option==1:
            loc = r"cs_170_small80.txt"
        elif option ==2:
            loc = r"Large-test-dataset.txt"
        elif option ==3:
            loc = r"cs_170_small15.txt"
        elif option ==4: 
            loc = r"cs_170_large15.txt"
        with open(loc) as datafile: #
            #line by line
            dataset_lines = datafile.readlines()
            #loop through lines
            for line in dataset_lines:
                #strip /n
                line = line.strip()
                #0th position is the class itself 1st list of features
                #regex to remove dbl space and space -. getting consistent , seperated values
                line = re.sub(r'(\ \ )+',',',line)
                line = re.sub(r'(\ \-)+',',-',line)
                #split on ,'s
                splitData = line.split(",")
                #convert data to floats
                floatData = []
                for x in splitData: 
                    floatData.append(float(x))
                #append lists of floats onto data resulting in a lists of lists
                self.dataset.append(floatData)
        #transpose data
        self.size=len(self.dataset)
        t_dataset = self.transpose(self.dataset)
        self.tsize = len(t_dataset)
        #calculate the default rate
        count1=0
        for x in t_dataset[0]:
            if x == 1.0:
                count1=count1+1
        count2 = self.size-count1
        if(count1>count2):
            self.defaultRate=count1/self.size
        else:
            self.defaultRate=count2/self.size

        #normalize data
        self.dataset = self.normalize(t_dataset)
        #print("dataset length = " , len(self.dataset))
        #print("prebook length = " , len(self.book))
        for x in self.dataset:
            class_data = x[0]
            x.pop(0)
            self.book.append((class_data,x))
        #print("postbook length = ", len(self.book))
        
    def test(self,row,subset_pos):
        current_closest= 9999999999
        current_class=-1
        #elements of test row
        obj2 = self.book[row][1]
        for x in self.book:
            temp=0
            if self.book.index(x) == row:
                continue
            else:
                #elements of 
                obj1=x[1]
                for y in subset_pos:
                    temp = temp + (obj2[y-1] - obj1[y-1])**2
                distance=math.sqrt(temp)
                if distance<current_closest:
                    current_closest=distance
                    current_class=x[0]
        return current_class

    #transposes a list of lists that is even
    def transpose(self,listslists):
        return list(map(list, zip(*listslists)))

    #takes a lists of lists that has been trasnposed
    def normalize(self,transposed):
        flag=True
        normedData=[]
        normedList=[]
        total=0
        for x in transposed:
            
            if flag:
                normedData.append(x)
                flag=False
            else:
                #compute mean
                total=0
                for a in x:
                    total = total +a                
                avg = total/len(x)
                # do you want to use another variable aside from y?
                numerator=0
                #compute std
                for b in x:
                    numerator = numerator + ((b-avg))**2
                total= numerator/len(x)
                std = math.sqrt(total)
                #normalize
                for c in x:
                    normedList.append(((c - avg)/std))
                normedData.append(copy.deepcopy(normedList))
                normedList.clear()
            #print(len(normedData))
        
        return self.transpose(normedData)