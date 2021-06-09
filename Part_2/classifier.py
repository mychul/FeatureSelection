class Classifier:
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
                features = class_of_data[1].split("  ")
                #TODO: normalize the data here
                #print(self.features)
                self.book.append((class_of_data[0],features))
        pass
    def Test(self):
        pass