from Part_2.classifier import *
from Part_2.validation import *
# test len(list)
# x = [(4,"happy"),(2,"sad"),(0,"hmmm")]
# print (max(x)[1])
# print(len(x))
# x = -1.0134041e-001
# tmp = round(float(x))
# print(tmp)
# driver for testing whether Validation can communicate with classifier
# classify = Classifier()
# classify.Train()
# test = Validator(classify)
# for item in test.classifier.book:
#     print(str(item))
subset=(3,5,)
classify = Classifier()
#classify.Train()
classify.Train2()
for x in classify.dataset:
    print(x)
#valid = Validator(classify)
#print(valid.validate(subset))
#print(classify.Test(4,(2,4,5,9)))