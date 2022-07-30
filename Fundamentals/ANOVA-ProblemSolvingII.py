"""
A reputed marketing agency in India has three different training programs for its project managers.
The three programs are Method – A, B, and C. To assess the success of the programs, 4 project managers from
each of the programs were sent to the field. Their project performance scores are given in the following table.

Test whether there is a significant difference among methods and among project managers.
Calculate the F0t and F0b at 5% significance level and select the appropriate option.
"""
"""
==========
Solution
==========

Null Hypotheses: 

H01 : μM1= μM2 = μM3 (for treatments)
That is, there is no significant difference among the three programs in their mean sales.
H02 : μS1 = μS2 = μS3 = μS4 (for blocks)

Alternative Hypotheses:

H11 : At least one average is different from the other, among the three programs.
H12 : At least one average is different from the other, among the four project managers.

Test Statistic

F0t(treatment) = MST / MSE
F0b(block)= MSB / MSE

Critical values

f(3, 6),0.05 = 4.7571 (for treatments)
f(2, 6),0.05 = 5.1456 (for blocks)

(i) Calculated F0t = 3.40 < f(3, 6),0.05 = 4.7571, the null hypothesis is not rejected and we conclude that there is a significant difference in the mean sales among the three programs.

(ii) Calculate F0b = 5.39 > f(2, 6),0.05 = 5.1456, the null hypothesis is rejected and concludes that there does not exist a significant difference in the mean sales among the four project managers.
"""
