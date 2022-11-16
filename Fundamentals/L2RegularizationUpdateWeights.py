"""
===========================
Problem statement
===========================
Given the 1d input and output vectors (X, Y). Use Gradient descent to get the optimal weights for the Linear regression model that uses Mean Squared Error(MSE) with L2 regularization.
The hypothesis function for Linear regression is Y_hat = wX + b.
The cost function = L(w)=
2n
1
​
 (∑
i=1
n
​
 (y
hat
i
​
 −y
i
 )
2
 +λ∑
j=1
d
​
 (w
j
2
​
 ))

Use the below functions to compute the gradient for a single weight w and bias b :

1. w's gradient =
n
1
​
 ∑
i=1
n
​
 ((Y
hat
i
​
 −Y
i
 )x
i
 +λw)
2. b's gradient =
n
1
​
 ∑
i=1
n
​
 (Y
hat
i
​
 −Y
i
 )

n is the number of samples,
d is the number of features,
λ here is the regularization parameter.
Complete the function to perform L2 regularization and return new updated weight w and bias b , rounded up to 2-decimal places.

===========================
Input Format:
===========================
Number of testcases.
For each testcase there will be two lines first will contain w and the second will be b.

===========================
Output Format:
===========================
For each testcase return the new updated weight w and bias b, rounded up to 2 decimal points
Sample Input:

1
2
1
Sample Output:

2.0 1.0
"""
import numpy as np


def L2_reg_update_weights(w, b, X, Y, learning_rate, lambda_value=1):
    """input: w is the coefficient of x in form of an integer.
              b is the constant term, integer format.
              X is a python list of input variables.
              Y is a python list of the output variables.
              learning_rate is in the form of float.
              lambda_value is an integer which is actually the penalty term in l2 regularization.
        output: You are required to return updated m and b upto two decimal points, in the same line.
    """

    X = np.asarray(X)
    Y = np.asarray(Y)

    w_deriv = np.mean((X * ((w * X + b) - Y) + lambda_value * w))
    b_deriv = np.mean(((w * X + b) - Y))

    # Update weights
    w -= learning_rate * w_deriv
    b -= learning_rate * b_deriv

    return (round(w, 2), round(b, 2))