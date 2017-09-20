
#change name of file to load in data from a different file.
def getData():
	x = []
	y = []
	input = open("data.txt").read().split("\n")
	for i in input:
		inputArray = i.split(",")
		exp = inputArray.pop(len(inputArray)-1)
		x.append(inputArray)
		y.append(exp)
	return x,y


X, y = getData()


