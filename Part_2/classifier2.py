import math
import re
class Classifier2:
    def __init__(self):
        self.book = []
    
    def Train(self): #TODO: filename/type to choose from
        with open(r"Part_2/cs_170_small80.txt") as datafile: #
            dataset_lines = datafile.readlines()
            for line in dataset_lines:
                line = line.strip()
                #0th position is the class itself 1st list of features
                class_of_data = line.split("  ", 1)
                #print(self.class_of_data[0])
                features = class_of_data[1].split(" ")
                class_of_data = round(float(class_of_data[0]))
                normedfeatures = []
                #TODO: normalize the data here
                for x in features: 
                    if x == "":
                        features.pop(features.index(x)) 
                for x in features: 
                    tmp = round(float(x))
                    #print(tmp) #debug
                    normedfeatures.append(tmp)
                #print(self.features)
                self.book.append((class_of_data,normedfeatures))
    def Test(self,row,subset_pos):
        current_closest= 9999999999
        current_class=-1
        obj2 = self.book[row][1]
        for x in self.book:
            temp=0
            if self.book.index(x) == row:
                continue
            else:
                obj1=x[1]
                for y in subset_pos:
                    temp = temp + (obj1[y] - obj2[y])**2
                distance=math.sqrt(temp)
                if distance<current_closest:
                    current_closest=distance
                    current_class=x[0]
        return current_class
