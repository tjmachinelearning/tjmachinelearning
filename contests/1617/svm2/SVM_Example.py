from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def getData(): #modify this to work with the data (hint: output is not the last thing but the....)
	x = []
	y = []
	input = open("data.txt").read().split("\n")
	for i in input:
		inputArray = i.split(",")
		exp = inputArray.pop(len(inputArray)-1)
		x.append(inputArray)
		y.append(exp)
	return x,y


x = [[0, 0], [1, 1]] # random input configuration (will get overwritten by getData())
y = [0, 1] # random output configuration (will get overwritten by getData())
x, y = getData()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)


#clf = svm.SVR(); # Regression SVM
clf = svm.SVC(kernel='rbf') # Uses linear kernel, alternate are: poly, rbf, sigmoid
# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC


clf.fit(x_train, y_train) #Train

# Test data
y_predict = clf.predict(x_test) # Runs through all of the test data and gives outputs in array

print(accuracy_score(y_test, y_predict)) # Gives % accuracy


