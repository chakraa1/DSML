"""
######################
Problem Description:
######################
A software firm claims that its employees, on average, earn about 200€ per hour.
A sample of 16 employees is selected and it's found that they have a mean salary of 190€ with a sample standard deviation of 30€.
Assuming the firm's claim to be true, what is the probability that the mean salary of the employees will be no more than 190€? (Approximately)
"""

"""
######################
Solution :
######################

Given population mean = 200
Sample mean = 190
Sample Standard deviation = 30
Sample size(n) = 16

Since n is small (<30) we can go for using the t-test here.

Using the data, the t-statistics value comes out to be
t-statistics = ( 190 - 200 ) / (30 / sq.root (16)) = -10 / 7.5 = -1.33

The degree of freedom here is, 16 - 1 = 15

Therefore, for a degree of freedom of 15, and t-statistics value of -1.33
Now we can use cdf to calculate p-value.

"""

import numpy as np
from scipy.stats import t

t_stat = (190 - 200) / (30 / np.sqrt(16))
dof = 16 - 1
print(t_stat)
p_value = (1.0 - t.cdf(abs(t_stat), dof))
print("p_value --> ", p_value)