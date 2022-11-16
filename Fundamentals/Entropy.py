"""
Given the list of "class" labels, complete the function to return the entropy rounded up to two decimal places.

Input Format:

A list
Output Format:

A float rounded off to 2 decimal places.
Sample Input:

[0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
Sample Output:

0.99
"""
import numpy as np


def entropy(y_target):
    '''
    Calculates the entropy given list of target(binary) variables
    '''
    # Write your code here

    # Initialize the entropy
    entropy = 0

    # calculate the counts of each unique element in the y_target
    counts = np.bincount(np.array(y_target))

    # Probabilities of each class label
    prob = counts / len(y_target)

    # Calculate the entropy involving all the unique elements
    for pct in prob:
        if pct > 0:
            entropy += (pct) * np.log2(pct)

    return np.round(-entropy, 2)