"""
Data distribution can be named based on the kurtosis value. Specifically, for given kurtosis k,

If k = 3, it is called a mesokurtic distribution and has kurtosis statistics similar to a normal distribution.
For k > 3, it is called a leptokurtic distribution (has a profound number of outliers)
And for k < 3, it is called a platykurtic distribution (shows lack of outliers).

Based on this information, given a data sample [4, 6, 2, 18, 7, 2], what would be this kind of distribution called?
"""
import numpy as np
from scipy.stats import kurtosis
data = np.array([4, 6, 2, 18, 7, 2])
print(kurtosis(data))

"""
k = ∑(x−x_mean)^4 / nσ^4
where,
x_mean = mean of the data
σ = standard deviation of the data
n = number of data points
x = element of the array

For the above given data distribution,
x_mean = 6.5
Using this, the numerator ∑(x−x_mean)^4 comes out to be 18349.38
Now the standard deviation comes out to be 5.47
Thus, nσ^4 = 5370.04
Dividing numerator / denominator, we get k = 3.417, or 3.2 (approx.)

Since k>3, this distribution is called a leptokurtic distribution.
"""