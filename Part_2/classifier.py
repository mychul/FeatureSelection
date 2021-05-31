class Classifier:
    def __init__(self):
        pass
    def Train(self):
        with open(r"Part_2/cs_170_small80.txt") as datafile:
            dataset_lines = datafile.readlines()
            for line in dataset_lines:
                line = line.strip()
                class_of_data = line.split("  ", 1)
                print(class_of_data[0])
                features = class_of_data[1].split("  ")
                print(features)
                #exit(0)
        pass
    def Test(self):
        pass


