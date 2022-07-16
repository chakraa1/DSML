import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import scipy

"""
##########################################################################
 Z-test - when we want to compare population means based on given sample
##########################################################################

#########################
Assumptions / Conditions 
#########################
    - Population mean and standard deviations are finite  
    - Standard deviation of population is known or can be estimated
    - Sample sizes are NOT too small (i.e.  > 30)

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

############################
Example - Problem Statement
############################
 The average hourly wage of a sample of 150 workers in plant 'A' was Rs.2·87 with a standard deviation of Rs. 1·08.  #
 The average wage of a sample of 200 workers in plant 'B' was Rs. 2·56 with a standard deviation of Rs. 1·28.        #
 Can an applicant safely assume that the hourly wages paid by plant 'B' are higher than those paid by plant ‘A’      #
 at a 5% significance level?                                                                                         #

"""
m1 = 2.87
m2 = 2.56
s1 = 1.08
s2 = 1.28
n1 = 150
n2 = 200

Tobs = (m1 - m2)/ np.sqrt(((s1**2)/n1) + ((s2**2)/n2)) # Tobs = Test statistics
print(Tobs) # 2.453
p_value = 2 * stats.norm.cdf(-Tobs) # considering symmetry at both side
print("p_value --> ", p_value)

"""
###################################################################
Conclusion  - How to interpret Z-test test statistics and p-value
###################################################################

Significance level = alpha = 5 % (given)
Two tail test is required as H0 has values at both sides
The distribution follows mean = 0 and standard deviation = 1
Now at 5% significance level , it supports 2 standard deviations = > 1* 2 = 2 ==> 0 + 2  (left) , 0 + 2 (right)
Also calculated T-statistics (Tobs) = 2.45 that is .45 beyond max standard deviation
Also calculated  p value (i.e. 0.014) is less than alpha (i.e. 0.05) 
Hence we can reject Null hypothesis

"""

"""
############################
Example - Problem Statement
############################
You are testing two drugs as a remedy. Drug A is effective on 41 out of a sample of 195. 
Drug B works on 351 out of 605 people. Are the two drugs comparable? Use 5% significance level for testing.
H0: The proportions are the same.
H1: The proportions are different.
Perform the two-proportion Z test.

"""


import numpy as np
from statsmodels.stats.proportion import proportions_ztest
count = np.array([41, 351])
nobs = np.array([195, 605])
stat, pval = proportions_ztest(count, nobs)
print('{0:0.3f}'.format(pval))

# z test statistic=8.99, H0 is rejected.


