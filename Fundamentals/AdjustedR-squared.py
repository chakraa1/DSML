"""
===============================
Problem Statement
===============================
Given the train and test data, fit a linear regression model on the train data and calculate the adjusted R-squared rounded up to 2 decimal places on the test data for this model.

===============================
Input Format:
===============================
4 lists representing the xtrain, ytrain, xtest and test.

===============================
Output Format:
===============================
A float rounded up to 2 decimal places

===============================
Sample Input:
===============================
xtrain = [[6, 9, 3], [4, 4, 8], [14, 3, 0], [5, 4, 12], [13, 10, 12], [2, 10, 2], [10, 3, 1], [13, 8, 7], [14, 0, 7], [11, 5, 3], [13, 14, 10], [12, 1, 3], [0, 9, 6], [12, 9, 11], [11, 8, 11], [2, 13, 3], [7, 0, 8], [14, 13, 5], [10, 5, 11], [4, 3, 13]]
ytrain = [10, 13, 28, 37, 27, 12, 24, 4, 7, 9, 8, 2, 1, 38, 35, 12, 8, 26, 10, 7]
xtest = [[9, 7, 8], [0, 5, 9], [8, 5, 9], [14, 5, 0], [8, 0, 1], [3, 6, 11], [2, 2, 11], [1, 7, 3], [8, 3, 14], [11, 14, 10]]
ytest = [16, 3, 18, 30, 16, 10, 22, 9, 6, 6]

===============================
Sample Output:
===============================
-1.14
"""

import numpy as np

# import linear regression model
from sklearn.linear_model import LinearRegression


def adj_rsq(xtrain, ytrain, xtest, ytest):
    xtrain = np.asarray(xtrain)
    ytrain = np.asarray(ytrain)
    xtest = np.asarray(xtest)
    ytest = np.asarray(ytest)

    # initialize the linear regression model
    reg = LinearRegression()

    # Train the model on train data
    reg.fit(xtrain, ytrain)

    # get the R-squared for the model for xtest and ytest
    r2_sq = reg.score(xtest, ytest)

    # calculate the adjusted R-squared using R-squared.
    # Adjusted R2 = 1 – [(1-R2)*(n-1)/(n-d-1)]
    adjr2_sq = 1 - ((1 - r2_sq) * (len(ytest) - 1) / (len(ytest) - xtest.shape[1] - 1))

    return np.round(adjr2_sq, 2)

xtrain = [[6, 9, 3], [4, 4, 8], [14, 3, 0], [5, 4, 12], [13, 10, 12], [2, 10, 2], [10, 3, 1], [13, 8, 7], [14, 0, 7], [11, 5, 3], [13, 14, 10], [12, 1, 3], [0, 9, 6], [12, 9, 11], [11, 8, 11], [2, 13, 3], [7, 0, 8], [14, 13, 5], [10, 5, 11], [4, 3, 13]]
ytrain = [10, 13, 28, 37, 27, 12, 24, 4, 7, 9, 8, 2, 1, 38, 35, 12, 8, 26, 10, 7]
xtest = [[9, 7, 8], [0, 5, 9], [8, 5, 9], [14, 5, 0], [8, 0, 1], [3, 6, 11], [2, 2, 11], [1, 7, 3], [8, 3, 14], [11, 14, 10]]
ytest = [16, 3, 18, 30, 16, 10, 22, 9, 6, 6]
print(adj_rsq(xtrain, ytrain, xtest, ytest))