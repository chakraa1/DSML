"""
=====================
Problem Description:
=====================
Given the training data, find out the best value for K between 1 and 10 (inclusive) for the multiclass classification
with KNN.

=====================
Input Format:
=====================

1) The first line contains the list of features for all the datapoints.
2) The second line contains the list of class to which the datapoints belong to
3) Finally the list of features of the query point is passed.

=====================
Output Format:
=====================

Returns the best value of K

=====================
Sample Input:
=====================
[[ 0.52, 26. ], [ 5.41, 39. ], [ 2.15, 8. ], [ 6. , 28. ], [ 0.96, 9. ]]
[0, 1, 2, 3, 4]
[[ 2.22, 21. ]]

=====================
Sample Output:
=====================
2

=====================
Input Explanation:
=====================

Data with 2 features and 5 classes are taken as two seperate input list.
A query point with two features is also taken as an input.
Output Explanation:

The optimal value of k = 2 is printed.

After doing all the hyperparameter tuning on the datapoints
"""

import numpy as np
# import kNN model from sklearn
from sklearn.neighbors import KNeighborsClassifier

X_train = np.asarray(X)
y_train = np.asarray(y)


def findOptimalK(X_train, y_train, x_q):
    error_rate = []
    k = []
    # define the range to which the value of k should go
    for i in range(1, 11):
        # set the value of k for the model
        knn = KNeighborsClassifier(n_neighbors=i)

        # fit the model on the training data
        knn.fit(X_train, y_train)
        # predict for the query point
        pred_i = knn.predict(x_q)

        # calculates the error of the model
        error_rate.append(np.mean(pred_i != y_train))

        # add the current value of k
        k.append(i)

    # find the index of the minimum error
    index = np.argmin(error_rate)

    # store the best k value which has minimum error
    best_k = k[index]
    return best_k
