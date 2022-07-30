"""
A Whirpool sales company has appointed four salesmen and they observe their sales through three different
seasons summer, winter, and monsoon the respective values are given below:

Perform analysis of variance with a 5% significance level to verify any significant differences in sales among salesman and in different seasons.
"""
import numpy as np
from scipy.stats import f_oneway

# sales person
A = np.array([45,43,39])
B = np.array([40,41,39])
C = np.array([38,45,41])
D = np.array([37,38,41])

# Conduct the one-way ANOVA
print("sales person",f_oneway(A, B, C,D))

# Seasons
summer = np.array([45,40,38.37])
winter = np.array([43,41,45,38])
monsoon = np.array([39,39,41,41])

# Conduct the one-way ANOVA
print("Seasons ",f_oneway(summer, winter, monsoon))

