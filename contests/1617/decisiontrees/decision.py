'''
    Nathaniel Choe
    Decision Trees
    TJML
    12/08/2016
'''

from sklearn import tree
import math

def p1():
    # look at sample data

    X = [[1, 2], [1, 4], [1, 5], [2, 3], [3, 4], [3, 5], 
         [1, 1], [2, 1], [3, 1], [4, 4], [4, 5], [5, 5],
         [4, 4], [5, 4], [4, 3], [5, 3], [5, 2], [4, 2],
         [4, 1], [5, 1]]

    Y = [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    clf = tree.DecisionTreeClassifier()
    clf =  clf.fit(X, Y)

    d_a = [[2.5, 5]]
    d_b = [[4.5, 2.7]]
    d_c = [[4.5, 5.]]
    d_d = [[2.1, 1.7]]

    #refer to sample graph in powerpoint for accuracy
    print(d_a, clf.predict(d_a))
    print(d_b, clf.predict(d_b))
    print(d_c, clf.predict(d_c))
    print(d_d, clf.predict(d_d))


def entropy():
    
    X = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4],
         [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]
    
    Y = [0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1]
    
    #two classes -> 1 or 0
    class_one = 0
    class_two = 0
    for item in Y:
        if item == 0:
            class_one += 1.0
        else:
            class_two += 1.0

    class_one_f = class_one / len(Y)
    class_two_f = class_two / len(Y)
    
    #entropy calculation -> H = sum(-f * log 2 f)
    H = -1 * (class_one_f * math.log(class_one_f, 2) + class_two_f * math.log(class_two_f, 2))
    print(H)


p1()
