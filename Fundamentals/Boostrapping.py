"""
=========================
Problem Description:
=========================
Given a list of random numbers representing a dataset, complete the program to perform the bootstrap sampling with sizes
 1, 10, and 100.
Print the mean of all the bootstrapped samples, after performing bootstrapping a certain number of times.

=========================
Input Format:
=========================
A list containing random numbers

=========================
Output Format:
=========================
Firstly the mean of the whole dataset is printed.
The mean of means of n_bootstrapped samples is printed for 1, 10, and 100 sizes.

=========================
Sample Input:
=========================
[5, 8, 9, 5, 0, 0, 1, 7, 6, 9, 2, 4, 5, 2, 4, 2, 4, 7, 7, 9]

=========================
Sample Output:
=========================
True Mean: 4.800
Samples=1, Estimated Mean: 2.000
Samples=10, Estimated Mean: 4.450
Samples=100, Estimated Mean: 4.880
"""
import numpy as np

dataset = eval(input())
dataset = np.asarray(dataset)


# It returns the mean of numbers list
def mean(numbers):
    return sum(numbers) / float(len(numbers))


# printing the mean of the dataset
print('True Mean: %.3f' % mean(dataset))


# It returns a 2d list consisting of the observations from the dataset representing the subsamples used in bootstrap sampling
def subsample(dataset, ratio=1.0):
    sample = list()
    n_sample = len(
        dataset) * ratio  # number of observations to draw from the dataset for the subsample according to dataset and ratio. It should be the rounded off integer.
    while len(sample) < n_sample:
        index = np.random.randint(0, len(dataset))  # pick a random index of observation from the dataset
        sample.append(dataset[index])  # append the observation to the list sample
    return sample


np.random.seed(1)

# ratio of the dataset we will be using to create to bootstrap samples
ratio = 0.10
for n_bootstrap in [1, 10, 100]:
    sample_means = list()  # list consisting of the mean of the bootstrap samples
    for i in range(n_bootstrap):
        sample = subsample(dataset, ratio)  # draw a sample from the dataset
        sample_mean = np.mean(sample)  # find the mean of the sample
        sample_means.append(sample_mean)

    # printing the means of each bootstrap sample
    print('Samples=%d, Estimated Mean: %.3f' % (n_bootstrap, mean(sample_means)))