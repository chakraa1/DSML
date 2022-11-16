"""
=======================
Problem Statement
=======================
Given two NumPy arrays, X representing the features and Y representing the target variables of shape (n, d) and (n, )
respectively, implement the closed-form solution of linear regression to return an array consisting of the values of
parameters rounded up to two decimal places. The shape of the returned parameter array should be (d,).

=======================
Input Format:
=======================

Two lists are taken as input.
First one is x which represents features
Second one is y which represents the target variable

=======================
Output Format:
=======================
A NumPy array with the values of parameters rounded up to two decimal places
Sample Input:

X = [[1.0, -0.17460021059294129], [1.0, 0.2655115856921195], [1.0, 0.004291430934033236], [1.0, 0.10854852571496944], [1.0, 1.331586504129518], [1.0, -0.7200855607188968], [1.0, -1.5454002921112682], [1.0, -0.008383849928522256], [1.0, 0.6213359738904805], [1.0, 0.7152789743984055]]
y = [4.79924308448553, 18.073015871023042, -5.993810986613133, -1.0756153061725424, 123.11324692336042, -40.6786526684709, -120.88605790017033, -3.020915122578166, 54.02764304916954, 65.68873810531909]

=======================
Sample Output:
=======================
[ 4.55 81.14]
"""
import numpy as np
def normal_eqn(X, y):
    ''' X is 2d list of shape (n,d) representing the values of d features for n samples
        y is a length n list representing the the values of target variables for n samples'''

    X = np.asarray(X)
    y = np.asarray(y)

    weight = np.array([])
    # YOUR CODE GOES HERE
    weight = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)

    return np.round(weight, 2)

X = [[1.0, -0.17460021059294129], [1.0, 0.2655115856921195], [1.0, 0.004291430934033236], [1.0, 0.10854852571496944], [1.0, 1.331586504129518], [1.0, -0.7200855607188968], [1.0, -1.5454002921112682], [1.0, -0.008383849928522256], [1.0, 0.6213359738904805], [1.0, 0.7152789743984055]]
y = [4.79924308448553, 18.073015871023042, -5.993810986613133, -1.0756153061725424, 123.11324692336042, -40.6786526684709, -120.88605790017033, -3.020915122578166, 54.02764304916954, 65.68873810531909]
print(normal_eqn(X,y))