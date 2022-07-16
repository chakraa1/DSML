"""
######################
Problem Description:
######################
Given two lists of heights of students of two classes, find whether their mean is significantly different or not. You are asked to use a T-test for independent samples.
Here the Null hypothesis is that the mean of both the samples is equal. Just return the t-stat and p-value after performing the t-test. The results about rejecting or not rejecting the null hypothesis are printed according to the code written in the solution suffix.

######################
Input Format:
######################
number of testcases
Space separated floats in two new lines representing two arrays for each test case.

######################
Output Format:
######################
Fail to reject the null hypothesis that concludes the means are equal/Reject the null hypothesis that concludes the means are unequal.
for each test case in a new line.Two lines will be printed, one for t_stat check and another for p_value check, one by one, for each test case.

######################
Sample Input:
######################
1
33.12 21.94 22.36 19.63 29.33 13.49 33.72 21.19 26.59 23.75
32.31 14.70 23.39 23.08 30.67 19.50 24.14 20.61 25.21 27.91

######################
Sample Output:
######################
Fail to reject the null hypothesis that concludes the means are equal.
Fail to reject the null hypothesis that concludes the means are equal.

######################
Note:
######################
Implement the t-test from scratch and return the t-stat and p-val
You are allowed to use functions like scipy.stats.sem(), sqrt(), scipy.stats.t.cdf(), but not scipy.stats.ttest_ind().
"""

# Importing Required Libraries
from math import sqrt
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from scipy.stats import sem
from scipy.stats import t
import numpy as np


def independent_ttest(data1, data2):
    '''
    input:
    data1 -> contains a python list signifying first data distribution
    data2 -> contains a python list signifying second data distribution
    output:
    t_stat -> a float value signifying the t_stat value
    p -> a float value signifying the p value
    '''
    t_stat = 0.0
    p = 0.0
    # ALLOWED to use "scipy.stats.sem(), sqrt(), scipy.stats.t.cdf()"
    # NOT allowed to use "scipy.stats.ttest_ind()"

    # YOUR CODE GOES HERE

    mean1, mean2 = mean(data1), mean(data2)
    std_error1, std_error2 = sem(data1), sem(data2)
    t_stat = (mean1 - mean2) / (sqrt(std_error1 ** 2 + std_error2 ** 2))
    dof = len(data1) + len(data2) - 2
    p = (1.0 - t.cdf(abs(t_stat), dof)) * 2

    # Your code ends here
    return t_stat, p

data1 = np.array([33.12,21.94,22.36,19.63,29.33,13.49,33.72,21.19,26.59,23.75])
data2 = np.array([32.31,14.70,23.39,23.08,30.67,19.50,24.14,20.61,25.21,27.91])
print(independent_ttest(data1, data2))