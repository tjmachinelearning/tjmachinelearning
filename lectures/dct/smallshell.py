def calculateImpurity(matrix):
    #do calculations
    return impurity

def splitmatrix(matrix, feature, threshold):

    #split matrix into leftchild, rightchild
    return leftchild, rightchild

def informationGain(parent, leftchild, rightchild):
    #do calculations
    return infoGain

def bestsplit(parent, depth):
    for each feature in parent:
        for each threshold in feature:
            lchild, rchild = splitmatrix(parent, feature, threshold)
            igain = informationGain(parent, lchild, rchild)

            #if igain is the greatest:
            #    save the leftchild, rightchild, feature, threshold

    #print this node (feature, threshold) of the decision tree
    # hint: use depth to indent
    #recur on leftchild
    #recur on rightchild