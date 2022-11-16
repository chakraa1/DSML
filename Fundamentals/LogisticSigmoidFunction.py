"""
A few of the characteristics of sigmoid function are:

Sigmoid is a monotonically increasing function
It increases rapidly near zero and plateaus as we reach the extreme ends
It maps the values in the range (-inf,inf) to a range (0,1)
Complete the function sigmoid() that calculates sigmoid values and derivates for the sigmoid values of the input NumPy array. The values in both arrays should be up to 2 decimal places.

Input Format :

A NumPy array
Output Format:

Two NumPy arrays, first consisting of the sigmoid values and the second consisting of the derivative of the sigmoid values
Sample Input:

[[3, 1], [0, 4]]
Sample Output:

[[0.95 0.73]
 [0.5 0.98]]
[[0.05 0.2 ]
 [0.25 0.02]]
Sample Explanation:

The first array is the sigmoid of the values in the input array and the second array is the values of derivatives of the sigmoid.
"""
import numpy as np


def sigmoid(x):
    '''x is a list
       Output -> Two numpy arrays are expected to be returned both with the same dimensions as of x'''

    x = np.asarray(x)

    # YOUR CODE GOES HERE
    sigmoid = np.round(1 / (1 + np.exp(-x)), 2)
    derivative_sigmoid = np.round(np.exp(-x) / (1 + np.exp(-x)) ** 2, 2)

    return sigmoid, derivative_sigmoid