from classifier import *

class validator:
    def __init__(self, classify_object):
        self.classifier = classify_object 
        
        self.counter = 0

    def validate(self,feature_subset):
        #print(self.classifier.book)# sanity check
        #print(len(self.classifier.book))
        self.counter=0
        for row in self.classifier.book:
            if self.classifier.test(self.classifier.book.index(row),feature_subset) == row[0]: 
                self.counter = self.counter + 1
        return self.counter/len(self.classifier.book)