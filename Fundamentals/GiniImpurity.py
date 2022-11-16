"""
Problem Description:

Given the class_vector in the form of a list consisting of the target variables for the observations, complete the function to return the gini impurity of the class_vector rounded up to two decimal places.

Note: The target variable is a binary variable (0/1)



Input Format:

A list containing the class labels for each sample
Output Format:

A float which is the gini-impurtiy rounded up to two decimal places
Example Input:

[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
Example Output:

0.49
Example Explanation:

1. GiniImpurity = 1−∑
j=0
K
​
 p
j
2
​
 , where p is the probability of class labels(K)

2. p
j
​
  is calculated as: p
j
​
 =
N
J
​
 , Where J is the number of samples of class label j and N is the total number of samples

Hence for class 0: p
0
​
 =
20
9
​
  and for class 1 : p
1
​
 =
20
11
​


Therefore GiniImpurity = 1−((
20
9
​
 )
2
 +(
20
11
​
 )
2
 )=0.49
"""

from collections import Counter
import numpy as np

def gini_impurity(class_vector):
    # Gini impurity = 1−∑pi2
    #dictionary with unique values and counts
    counts = Counter(class_vector)

    #probability of class 0
    prob_zero = counts[0]/len(class_vector)

    #probability of class 1
    prob_one = counts[1]/len(class_vector)

    #probability square sum
    prob_sqrsum = prob_zero ** 2 + prob_one ** 2

     #Calculate the gini impurity
    gini_imp = 1 - prob_sqrsum

    return np.round(gini_imp,2)