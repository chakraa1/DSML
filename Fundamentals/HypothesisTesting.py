import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

#########################################################
# Experiment # 1 t: Toss the coin 100 times             #
#########################################################

# Test statistic: Count the number of heads
# H0: Coin is fair
# Ha: Coin is unfair
# T ~ Binomial(n=100, p=0.5) under Null Hypothesis(=H0)
prob = stats.binom.cdf(k=25, n=100, p=0.5) + (1 - stats.binom.cdf(k=75, n=100, p=0.5))
print(prob) # P( T<=30 or T>=70  | H0 )
#########################################################
# P-value - 3.723142327660961e-07 ==> Very low than 5 %
# Hence we can reject H0
#########################################################

####################
# Experiment # 2   #
####################
# H0: Coin is fair
# Ha: Coin is biased towards heads
###################################################################################################################
# Q1. You flip an unfair coin multiple times, and it lands on heads 60% of the time.                              #
# Considering the 95% confidence interval, how many flips are needed to detect that the coin is unfair?           #
###################################################################################################################

prob20 = stats.binom.cdf(k=20, n=100, p=0.6)
prob93 = stats.binom.cdf(k=93, n=100, p=0.6) # Ho accepted
prob50 = stats.binom.cdf(k=50, n=100, p=0.6)
prob47 = stats.binom.cdf(k=47, n=100, p=0.6)

print(prob20,prob93,prob50,prob47)

################################################################################################
# P value - 3.420435841660837e-16 0.9999999999999925 0.027099197757009075 0.005760648048002624
################################################################################################



