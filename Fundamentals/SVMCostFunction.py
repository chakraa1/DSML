"""
=========================
Problem Description
=========================
John is an Electronics Major, and he has to deal with Logic gates daily. Being inclined toward Machine Learning, he wants to implement and test maximum margin classifiers on various logic gate problems. He decided to go with SVM and optimize the hinge loss to maximize the decision margin. Also wants to make his model prevents overfitting, hence wants to implement regularization too. Given M data points for logic gates, relative weights of trained SVMs, and the C parameter, help him calculate the regularized cost for the gates.

Hinge Loss
In machine learning, the hinge loss is a loss function used for training classifiers. The hinge loss is used for "maximum-margin" classification, most notably for support vector machines (SVMs). It is given as:


Cost function
With L2 regularization applied, for some n data points the cost function is given as follows :
J(w,b)=
2
∣∣w∣∣
​
 +C
n
1
​
 ∑
i=1
n
​
 max(0,1−y∗(w.x
i
​
 +b))
In order to help him, you just need to complete the cost function for given data points, weights, the C parameter, and the labels.
STDIN and STDOUT are taken care of.
=========================
Input Format
=========================
There are 4 inputs:
weights: Learned weights of the support vector machines
inps: Data points of logic gates
labels: Logic gate results i.e. labels of the data points
C: Penalty parameter that controls the margin of the support vectors.
=========================
Output Format
=========================
It will be the cost value return by the svm_cost function.

=========================
Example Input
=========================
W = [0.5,0.5]
X=[[0,0],[0,1],[1,0],[1,1]]
Y=[0,0,0,1]
C=1.0

=========================
Example Output
=========================
0.927

=========================
Example Explanation
=========================
0.927 is the value returned by the Cost Function formula

Note
Return the rounded cost up to 3 decimals.
Labels are only binary, hence can be considered as a binary classification problem.
"""
import numpy as np


def svm_cost(weights, inps, labels, C):
    """
    weights: weights learned by the SVM model
    inps   : input data points
    labels : corresponding labels
    C      : Penalty parameter
    """
    cost = 0
    x = np.array(inps)
    y = np.array(labels)
    weights = np.array(weights)
    zero = np.zeros(y.shape[0])

    # YOUR CODE GOES HERE

    n = x.shape[0]
    y_pred = np.dot(x, weights)
    hinge_loss = C * ((sum(np.maximum(zero, 1 - y * y_pred))) / n)
    cost = np.linalg.norm(weights) + hinge_loss

    # CODE ENDS HERE
    return round(cost, 3)
