from classifier import *
from validation import *
import time

print("Welcome to 861126014 (Michael Chiang) & 861199635 (Tinh La) group's part 2 for feature selection project.\n")
tic=time.perf_counter()
subset=(2,4,6)
small_classify = Classifier()
small_classify.Train()
valid = Validator(small_classify)
tock=time.perf_counter()
print("Using 3,5,7 as the feature subset on the small data set we get an accuracy of", valid.validate(subset))
print("Finished processing in "+ str(tock-tic) + " seconds") 
subset=(0,14,26)
big_classify = Classifier()
big_classify.Train2()
valid = Validator(big_classify)
tock2=time.perf_counter()
print("Using 1,15,27 as the feature subset on the small data set we get an accuracy of", valid.validate(subset))
print("Finished processing in "+ str(tock2-tic) + " seconds")