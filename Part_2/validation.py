from Part_2.classifier import *

class Validator:
    def __init__(self, classify_object):
        self.classifier = classify_object 
        self.counter = 0

    def validate(self,feature_subset):
        #print(self.classifier.book)# sanity check
        for x in self.classifier.book:
            for y in self.classifier.book:
                # case where it's the same row
                if x == y: 
                    continue
                else:
                    # TODO: inputs for Test: feature_subset, x
                    if self.classifier.Test() == x[0]: 
                        self.counter = self.counter + 1
        return self.counter/len(classifier.book)

