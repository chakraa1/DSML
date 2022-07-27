"""
======================
Problem statement
======================
The below CSV file contains percentile for the same values occuring in different distributions.
CSV file : percentiles.csv
Find the value of Tobs (round off to 2 decimal place).
(Run Python code on local engine)

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
from matplotlib.pyplot import figure
import warnings


df = pd.read_csv("walmart_data.csv")
