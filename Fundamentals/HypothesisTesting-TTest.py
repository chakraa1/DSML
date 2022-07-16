"""
##########################################################################
 t-test - when we want to compare population means based on given sample
##########################################################################

##############################
Properties of T-distribution
##############################
    - Centered at zero
    - Symmetric
    - Degrees of freedom (v > 0) - defines the shape of the curve
        - If DOF increases to very large (higher pick and lesser tail) ==> t-distributions tends to Z-distribution
        - v = n1 + n2 -2
#########################
Assumptions / Conditions
#########################
    - Population mean and standard deviations are finite
    - Standard deviation of population is known or can be estimated
    - Sample sizes are too small (i.e.  < 30)

############################
Alternate options to Z-test
############################
    - Approach # 2 : Calculate Confidence Interval (95%)  type of test for a given sample  - compare mu1 amd mu 2 [Only mean can be compared]
    - Approach # 3 : Population median 1 vs Population median 2 (Tricky though)
    - Approach # 4 : QQPlot approach - distribution1  != distribution2
    - Approach # 5 : KS test (uses gap between CDFs) - compared distribution


########################################
Scenarios and type of Tail test (1-tail vs 2-tail)
########################################
Ho = mu1 = mu2
Ha = mu1 != mu2  [two tail]
Ha = mu1 > mu2   [one tail]
Ha = mu1 < mu2   [one tail]

################################
Example #1 - Problem Statement
################################
There are 8 females and 12 males in a coaching class. After a practice test, the coach wants to know whether the average
score of females is greater than the average score of males. Given data describes the scores of females and males.
Check whether the assumption of the coach is significant or not at a 5% of significance level?

female_scores=[25,30,45,49,47,35,32,42]
male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]                                                                                    #

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import scipy

female_scores=np.array([25,30,45,49,47,35,32,42])
male_scores=np.array([45,47,25,22,29,32,27,28,40,49,50,33])

#T-Test
n1 = 8
n2 = 12
dof = n1 + n2 - 2
dof
print("degrees of freedom --> ",dof)

diff_means = female_scores.mean() - male_scores.mean()
diff_means

#2 sample t-test
tstats = stats.ttest_ind(female_scores, male_scores)
print(tstats)

"""
###########
Conclusion 
###########
Failed to reject null hypothesis as p-value (0.5694047618891788) is more than alpha (.05)

"""


""""
################################
Example #2 - Problem Statement
################################
The Zumba trainer claims that the new dance routine helps to reduce more weight of the customers. 
The weights of 8 people are recorded for last month before and for this month after the Zumba training. 
Test the trainer's claim with 90% confidence.

wt_before=[85, 74, 63.5, 69.4, 71.6, 65,90,78]
wt_after=[82, 71, 64, 65.2, 67.8, 64.7,95,77]

"""
wt_before=[85, 74, 63.5, 69.4, 71.6, 65,90,78]
wt_after=[82, 71, 64, 65.2, 67.8, 64.7,95,77]
tstats_wt = stats.ttest_ind(wt_before, wt_after)
print("tstats_wt ==> ", tstats_wt)

"""
###########
Conclusion 
###########
Failed to reject null hypothesis as p-value (0.81200) is more than alpha (.1 i.e. 90 % confidence level)
"""

"""
################################
Example #3 - Problem Statement
################################
A software firm claims that its employees, on average, earn about 200€ per hour. 
A sample of 16 employees is selected and it's found that they have a mean salary of 190€ with a sample standard deviation of 30€. 
Assuming the firm's claim to be true, what is the probability that the mean salary of the employees will be no more than 190€? (Approximately)

"""
mu = 200

m1 = 190
m2 = 200
s1 = 30
s2 = 0
n1 = 16
n2 = 0

Tobs = (m1 - m2)/ np.sqrt(((s1**2)/n1) + ((s2**2)/n2)) # Tobs = Test statistics
print(Tobs) # 2.453
p_value = 2 * stats.norm.cdf(-Tobs) # considering symmetry at both side
print("p_value --> ", p_value)

"""
###########
Conclusion 
###########
Failed to reject null hypothesis as p-value (0.XXXXX) is more than alpha (.1 i.e. 90 % confidence level)
"""


