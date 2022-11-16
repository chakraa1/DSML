"""
========================
Problem statement
========================
As you know, a Decision Tree is all about splitting nodes at different levels and trying to do predictions accurately.

Given features and labels/targets, determine which feature is best to split upon at the first root level for building a
decision tree.

Note : The features are binary(containing 0 or 1 only) whereas targets are continuous in nature (regression) So,
the main task is to determine which attribute/feature is best to split upon considering the regression task taking the loss as "Residual sum of squares".

========================
Input Format :
========================
Two nd-arrays representing features and labels/targets respectively are taken as input

========================
Output Format :
========================

An integer representing the feature index of the feaure on which we can split the decision tree
Sample Input:

features: array([[1, 1],[0, 1],[1, 1],[1, 1],[0, 1],[0, 0],[1, 1],[0, 0],[1, 0],[1, 1]])
targets: array([ 1.02721641, -0.25072461, -1.56434949,  1.15213561,  1.34919707,
            -1.35253951, -0.17552063, -0.45909391, -0.10864444,  0.83352153])

========================
Sample Output:
========================
2
Explanation: In the above-mentioned example, since there is a 2D array present having a size of (10,2), there are 2 attributes here

If we split on Attribute1: Then if you compute the residual sum of squares, it would be computed as 0.913 and for Attribute2, RSS will be 0.745. You have to return your answer considering 1-based indexing. So you have to return 2 as your final answer.
"""
import numpy as np


def best_split(features, targets):
    '''
    inputs:
        features: nd-array
        labels: nd-array
    output:
        integer value determining best attribute idx (1-based indexing) for decision tree regression
    '''

    best_feature_idx = None
    best_value = None
    mse_base = 1e9

    # iterating through each of the feature
    for feature_idx in range(features.shape[1]):
        # Observations in left and right of the node
        left_y = targets[np.where(features[:,
                                  feature_idx] == 0)]  # left node will have all the target values of observations in which feature_idxth feature is 0
        right_y = targets[np.where(features[:,
                                   feature_idx] == 1)]  # left node will have all the target values of observations in which feature_idxth feature is 1

        # calculate the means
        left_mean = np.mean(left_y)
        right_mean = np.mean(right_y)

        # calculate the left and right residuals
        res_left = np.sum([(act - left_mean) ** 2 for act in left_y])
        res_right = np.sum([(act - right_mean) ** 2 for act in right_y])

        # Calculate the mse
        # YOUR CODE GOES HERE
        mse_split = res_left / len(left_y) + res_right / len(right_y)

        # YOUR CODE ENDS HERE
        # Checking if this is the best split so far
        if mse_split < mse_base:
            best_feature_idx = feature_idx

            # Setting the best gain to the current one
            mse_base = mse_split
    return best_feature_idx + 1  # For 1-based indexing