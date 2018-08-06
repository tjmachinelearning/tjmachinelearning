import numpy as np
def impurity(node):
    #gini impurity
    ginisum = 0.0
    class_values = list(set([sample[-1] for sample in node]))
    for c in class_values:
        ratio = [sample[-1] for sample in node].count(class_value) / float(len(node))
        #sample[-1] is the sample's class value
            
        ginisum += ratio*ratio
            
    return (1.0 - ginisum)

def information_gain(parent, leftchild, rightchild):
    return impurity(parent) - (len(leftchild)/len(parent))*impurity(leftchild) \
           - (len(rightchild)/len(parent))*impurity(rightchild)

def split(parent, feature, threshold):
    left = []
    right = []
    for row in parent:
        if row[feature] < threshold:
            left.append(row)
        else:
            right.append(row)
    return left, right

def best_split(parent):
    leftchild = None #placeholders
    rightchild = None
    ig = 0.0
    for feature in range(len(parent)-1): #last element is class value, not feature
        for threshold in [
            np.percentile(parent[:, feature], quartile) for quartile in [20, 40, 60, 80]]:
            if leftchild:
                p_leftchild, p_rightchild = split(parent, feature, threshold)
                p_ig = information_gain(parent, p_leftchild, p_rightchild)
                if p_ig > ig: #check if new split yields greater information gain
                    leftchild = p_leftchild
                    rightchild = p_rightchild
                    ig = p_ig
            else:
                leftchild, rightchild = split(parent, feature, threshold)
                ig = information_gain(parent, leftchild, rightchild)
    return leftchild, rightchild
    
        
