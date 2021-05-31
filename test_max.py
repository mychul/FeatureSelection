from Part_2.classifier import *
x = [(4,"happy"),(2,"sad"),(0,"hmmm")]
print (max(x)[1])
print(len(x))
test = Classifier()
test.Train()
for item in test.book:
    print(str(item) + '\n')
#print(test.book)