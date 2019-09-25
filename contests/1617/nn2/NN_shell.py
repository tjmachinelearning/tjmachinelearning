# Nikhil Sardana and Mihir Patel, 2/15/17

# ----------- This Shell --------------------------------
# This shell code demonstrates the MLP classifier (Neural Network)
# training using Scikit-Learn. This sample uses the MNIST data.
# Run it.
# Play around with the parameters to increase the accuracy.
# -------------------------------------------------------

# ----------- Your Task ---------------------------------
# Modify the shell to take in the mushroom data.
# (You may want to refer to the SVM shell for data input)
# Use 25% of the data for testing.
# Tune the hyperparameters to increase your accuracy.
# --------------------------------------------------------


from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier

mnist = fetch_mldata("MNIST original")
# rescale the data, use the traditional train/test split
X, y = mnist.data / 255., mnist.target
#splitting the training and testing data
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


#classifier
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)
# train network
mlp.fit(X_train, y_train)
print("Training set score: %f" % mlp.score(X_train, y_train)) # training accuracy
print("Test set score: %f" % mlp.score(X_test, y_test)) # testing accuracy
