import numpy as np; import math
import random
import csv

class Layer(object):
    def __init__(self, llen):
        self.len = llen #layer size
	#initialize bias, weights, etc. use numpy vectors/arrays

class NeuralNetwork(object):
    def __init__(self, layers):
        self.layers = layers #list of Layers
	       #initializations

    def forwardprop(self, input_vector):
        sigmoid = lambda val: 1.0/(1.0 + np.exp(-val))
        #forward propogate thru layers


    def backprop(self, y):
        sigmoid = lambda val: 1.0/(1.0 + np.exp(-val)) 
        sig_deriv = lambda val: (1-sigmoid(val))*sigmoid(val) 
        #Calculate gradients
        #Update weights 


def train(neuralnet, iterations, training_data):
    for j in range(iterations): #number of iterations, to be tuned
        #train (forward, backprop)

def test(neuralnet, testing_data):
	for data_point in testing_data:
	    #get output for each data_point
        #compare output to ground truth


n = Network(["""list of layers"""])
#data i/o
#train network
#test network