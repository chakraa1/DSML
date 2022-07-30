import numpy as np
from scipy.stats import f_oneway

def anova1(samp1, samp2, samp3, samp4):
    '''
    input:
    samp1, samp2, samp3, samp4 -> each of these variables is a python list of 5 integers
    output:
    t_stat -> just return the calculated test statistic as per one-way annova
    '''
    t_stat = 0.0

    k = 4  # number of different samples
    n = len(samp1) * k  # total number of observations

    total_sum = samp1.sum() + samp2.sum() + samp3.sum() + samp4.sum()

    total_sum_square_average = np.square(total_sum) / n  # total sum square average
    average_of_sum_of_squares_for_each_group = (np.square(samp1.sum()) + np.square(samp2.sum()) + np.square(samp3.sum()) + np.square(samp4.sum())) / samp1.size  # average of sum of squares for each group
    sum_of_square_of_each_element = np.square(samp1).sum() + np.square(samp2).sum() + np.square(samp3).sum() + np.square(samp4).sum()  # sum of square of each element

    sum_of_squares_between_groups = average_of_sum_of_squares_for_each_group - total_sum_square_average  # sum of squares between groups
    sum_of_squares_within_groups = sum_of_square_of_each_element - average_of_sum_of_squares_for_each_group  # sum of squares within groups

    MSB = sum_of_squares_between_groups / (k - 1)  # variance between groups
    MSW = sum_of_squares_within_groups / (n - k)  # variance within groups

    t_stat = (MSB / MSW)

    return t_stat

samp1 = np.array([8,10,12,8,7])
samp2 = np.array([12,11,9,14,4])
samp3 = np.array([18,12,16,6,8])
samp4 = np.array([13,9,12,16,15])

print("ANOVA scratch t stats ", anova1(samp1, samp2, samp3, samp4))
print("ANOVA f_oneway(scipy.stats) t stats ", f_oneway(samp1, samp2, samp3, samp4))