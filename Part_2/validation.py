from Part_2.classifier import *

class Validator:
    def __init__(self, classify_object):
        self.classifier = classify_object 
        self.classifier.Train()
        self.counter = 0

    def validate(self,feature_subset):
        #print(self.classifier.book)# sanity check
        #print(len(self.classifier.book))
        for row in self.classifier.book:
            # TODO: inputs for Test: feature_subset, x
            if self.classifier.Test(self.classifier.book.index(row),feature_subset) == row[0]: 
                self.counter = self.counter + 1
        return self.counter/len(self.classifier.book)