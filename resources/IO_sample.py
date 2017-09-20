
#change name of file to load in data from a different file.
#for testing data (no labels)
def getDataUnlabeled():
    x = []
    input = open("test.csv").read().split("\n")
    for index, i in enumerate(input):
        inputArray = i.split(",")
        if(index==0):
            inputArray[0] = '4'
        if(len(inputArray)==9): #number of features           
            x.append(inputArray)
        else:
            print(len(inputArray))
    return x

#change name of file to load in data from a different file.
#for training data (with labels)
def getDataLabeled():
    x = []
    y = []
    input = open("train.csv").read().split("\n")
    for i in input:
        inputArray = i.split(",")
        if(len(inputArray)==10): #number of features + number of labels        
            exp = inputArray.pop(len(inputArray)-1)
            x.append(inputArray)
            y.append(exp)
        else:
            print(len(inputArray))
    return x,y



X_train, y_train = getDataLabeled()
X_test = getDataUnlabeled()

