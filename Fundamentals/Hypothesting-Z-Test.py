import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import scipy
#######################################################################################################################
# The average hourly wage of a sample of 150 workers in plant 'A' was Rs.2·87 with a standard deviation of Rs. 1·08.  #
# The average wage of a sample of 200 workers in plant 'B' was Rs. 2·56 with a standard deviation of Rs. 1·28.        #
# Can an applicant safely assume that the hourly wages paid by plant 'B' are higher than those paid by plant ‘A’      #
# at a 5% significance level?                                                                                         #
#######################################################################################################################
m1 = 2.87
m2 = 2.56
s1 = 1.08
s2 = 1.28
n1 = 150
n2 = 200

Tobs = (m1 - m2)/ np.sqrt(((s1**2)/n1) + ((s2**2)/n2)) # Tobs = Test statistics
print(Tobs) # 2.453

###############################################
# Significance level = alpha = 5 %
# Two tail test is required as h0 has values at both sides
# The distribution follows mean = 0 and standard deviation = 1
# Now at 5% significance level , it supports 2 standard deviations = > 1* 2 = 2 ==> 0 + 2  (left) , 0 + 2 (right)
# Hence , 2.45 will be .45 beyond max standard deviation
# Hence we can reject Null hypothesis
###############################################