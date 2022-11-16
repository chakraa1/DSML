"""
=======================
Problem Statement
=======================
Given the data x (x[i] represents the values of independent variables for each ith observation) and y (y[i]
represents the value of the dependent variable for ith observation), w (representing the starting values of weights),
alpha (learning rate), and nitr(number of iterations),
complete the program to calculate the updated values of weights after nitr iterations of batch gradient descent.
Note: In this particular question consider the value of intercept (w
0
​
 ) to be zero and the loss function is just the difference between y_pred and y.
 The w should be rounded off to two decimal places.
=======================
Input Format:
=======================
The first three inputs will be lists for x, y, and w.
Then there will be two more inputs representing alpha and nitr.

=======================
Output Format:
=======================
A NumPy array for updated values of w

=======================
Example Input:
=======================
x = [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0], [1.0, 4.0], [1.0, 5.0], [1.0, 6.0], [1.0, 7.0], [1.0, 8.0], [1.0, 9.0]]
y = [26.75, 29.12, 36.46, 32.82, 30.46, 39.7, 35.52, 39.84, 36.83, 42.74]
w = [1.0, 1.0]
alpha = 0.0005
nitr = 10

=======================
Example Output:
=======================
[1.14 1.64]

Example Explanation:

When x= [1.0, 0.0] , y = [26.75] and w = [1.0, 1.0]

y_pred = w×x
t
 =1.0×1.0+0.0×1.0=1.0

loss = y_pred-y = 1.0 - 26.75 = -25.75

Gradient =
NewWeight = w - alpha × Gradient
NewWeight = w - alpha × Gradient

"""

import numpy as np


def gradient_descent(x, y, w, alpha, nitr):
    x = np.asarray(x)
    y = np.asarray(y)
    w = np.asarray(w)

    xTrans = x.transpose()

    # Perform Gradient descent on data nitr times
    for i in range(0, nitr):
        # calculate the output of y_pred using weights
        y_pred = np.dot(x, w)

        # Calculate the difference between y_pred and y
        loss = y_pred - y

        # average the gradient
        gradient = np.dot(xTrans, loss) / len(x)

        # Update the weights
        w = w - alpha * gradient

        # round off the values in array to two decimal places
    return np.round(w, 2)

x = [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0], [1.0, 4.0], [1.0, 5.0], [1.0, 6.0], [1.0, 7.0], [1.0, 8.0], [1.0, 9.0]]
y = [26.75, 29.12, 36.46, 32.82, 30.46, 39.7, 35.52, 39.84, 36.83, 42.74]
w = [1.0, 1.0]
alpha = 0.0005
nitr = 10

print(gradient_descent(x, y, w, alpha, nitr))