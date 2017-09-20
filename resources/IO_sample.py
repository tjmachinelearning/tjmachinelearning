
#change name of file to load in data from a different file.
def getData():
    x = []
    y = []
    input = open("training_xd.csv").read().split("\n")
    for i in input:
        inputArray = i.split(",")
        if(len(inputArray)==10): #num of features + num of labels
            exp = inputArray.pop(len(inputArray)-1)
            x.append(inputArray)
            y.append(exp)
        else:
            print(len(inputArray))
    return x,y



X, y = getData()


