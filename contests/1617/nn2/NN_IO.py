import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

def char_position(letter):
    return ord(letter) - 97
def getData():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input = open("agaricus-lepiota.data.txt").read().split("\n")
    x = []
    y = []
    j=0;
    for i in input:
        j+=1
        #print(j)
        inputArray = i.split(",")
        for k in range (len(inputArray)):
            inputArray[k] = char_position(inputArray[k]) # convert characters to numbers
        exp = inputArray.pop(0)
        x.append(inputArray)
        y.append(exp)
    return x,y
 
mnist = fetch_mldata('MNIST original')

# rescale the data, use the traditional train/test split
x, y = mnist.data / 255., mnist.target
x_train, x_test = x[:60000], x[60000:]
y_train, y_test = y[:60000], y[60000:]

#my_x, my_y = getData()
#x_train, x_test, y_train, y_test = train_test_split(my_x, my_y, test_size=0.25, random_state=42)

# hidden_layer_sizes = network, 
# activation = function, alpha = L2 Parameter
# batch_size = batch size
# learning_rate = constant/adaptive
# max_iter = max iter
# tol = improve at least this much in 2 consec iterations
# learning_rate_init=.001
# verbose = debug/print
# early_stopping = tests similar to tol except on trian set
# validation_fraction = fraction for early_stopping
mlp = MLPClassifier(hidden_layer_sizes=(5,), #(10,10)
                    activation='logistic', 
                    alpha=0.0001, 
                    batch_size='auto', 
                    learning_rate='constant', 
                    learning_rate_init=0.001, 
                    max_iter=200, 
                    shuffle=True, tol=0.0001, 
                    verbose=True, 
                    early_stopping=False, 
                    validation_fraction=0.1)

mlp.fit(x_train, y_train)
print("Training set score: %f" % mlp.score(x_train, y_train))
print("Test set score: %f" % mlp.score(x_test, y_test))