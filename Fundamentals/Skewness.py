"""
For a negatively skewed distribution, mean<median<mode
For distribution with no skewness(Normal), mean=median=mode
For a positively skewed distribution, mean>median>mode
"""

import numpy as np
import statistics as stat

data = np.array([38,36,31,30,20,28,25,26,19,21,19,21,20,21,21,20,21,24,32,35,38,38])
print("mean", data.mean(),"median ", np.median(data),"mode",stat.mode(data))

#mean: 26.54, median: 24.5 ,mode: 21
# for which mean > median > mode.So,Right Skewed.
