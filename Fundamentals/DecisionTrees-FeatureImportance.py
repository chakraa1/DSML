"""
=======================
Problem statement
=======================

Given the Gini-impurities of the nodes and their children for all the splits where a feature f is used for splitting,
complete the function to return the feature importance of f rounded up to 2 decimal places.

total is the total number of data points in the dataset. datapnts_at_splits[i] represents the number of points available
 at the ith node where the feature f is used for splitting. impurities[i] represents the Gini-impurities of the node, left child, and right child at the ith node where feature f is used for splitting.

=======================
Input Format:
=======================

An integer (total)
A list (datapnts_at_splits)
A 2d-list (Gini-impurities)

=======================
Output Format:
=======================

A float (rounded up to 2 decimal places)

=======================
Sample Input:
=======================
total = 1000
datapnts_at_splits = [443, 426, 397, 390, 382, 306, 208, 160, 97, 91]
impurities = [[0.84, 0.97, 0.06], [0.75, 0.19, 0.96], [0.97, 0.74, 0.44], [0.42, 0.23, 0.05], [0.93, 0.89, 0.06], [0.37, 0.17, 0.94], [0.24, 0.79, 0.99], [0.87, 0.88, 0.32], [0.35, 0.03, 0.75], [0.72, 0.77, 0.22]]
Sample Output:

Feature Importance = -0.96
"""

import numpy as np


def feature_imp(total, datapnts_at_splits, impurities):
    '''
    total: It represents the total number of points in the dataset
    datapnts_at_splits is the list consisting of datapoints present at the each node of the tree where feature f is used for splitting
    impurities is a 2d list consisting of the Gini-impurities of the parent, left child and right child for such nodes where feature f is used for splitting
    '''

    importance = 0

    for i in range(len(datapnts_at_splits)):
        parent_impurity = impurities[i][0]
        left_child_impurity = impurities[i][1]
        right_child_impurity = impurities[i][2]

        information_gain = parent_impurity - (left_child_impurity + right_child_impurity)

        importance += information_gain * datapnts_at_splits[i] / total

    return np.round(importance, 2)