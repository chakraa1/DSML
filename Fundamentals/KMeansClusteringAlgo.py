"""
==================
Problem statement
=================
Given the initialized centroids and points, complete the k_means() function to return the updated centroids after 10 iterations.

===============
Input Format:
===============
Two lists are taken as input representing points and initialized centroids

===============
Output Format:
===============
Strings are printed representing centroids for each of the ith iteration.

===============
Sample Input:
===============
points = [(1,2),(3,4),(1,4),(0,4),(0,5),(-2,4),(-3,5),(6,-8),(5,6),(-1,-2),(3,-5),(4,-8),(5,-10),(-4,-4),(-2,-1),(0,0),(-3,0),(3,3),(4,4),(1,2),(6,7),(-9,0)]
centroids = [(1,1),(-1,1),(-1,-1)]

===============
Sample Output:
===============
Centroids after 1th iteration: [(2.18, 3.73), (-4.25, 2.25), (1.57, -5.43)]
Centroids after 2th iteration: [(2.18, 3.73), (-3.8, 1.6), (2.17, -6.17)]
Centroids after 3th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 4th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 5th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 6th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 7th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 8th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 9th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
Centroids after 10th iteration: [(2.4, 4.1), (-3.0, 0.25), (4.5, -7.75)]
"""

# points is the list of tuples consisting of coordinates of points.
# centroids is the list of tuples consisting of coordinates of centroid points
import numpy as np


# Function to calculate the distance between two points
def calc_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


# Function to update the centroids of a cluster lst
def upd_centroid(lst):
    val_x, val_y = 0, 0
    for x, y in lst:
        val_x += x
        val_y += y
    return (np.round(val_x / len(lst), 2), np.round(val_y / len(lst), 2))


# Perform the k-means algorithm to cluster the points
def k_means(points, centroids):
    # groups is a 2d list where groups[i] will have all the points corresponding to the ith cluster
    groups = [[] for i in range(len(centroids))]
    for pnt in points:

        # tmp is a list to store the distance of points from each centroid. tmp[j] is the distance of jth centroid from pnt
        tmp = [0] * len(centroids)

        for i, centroid in enumerate(centroids):
            tmp[i] = calc_dist(pnt, centroid)

        # calculate the minimum distance from a centroid from all the centroid distances
        min_d = min(tmp)

        # find the index of minimum distance from tmp
        group_id = tmp.index(min_d)

        # store the point into the sublist of that nearest centroid
        groups[group_id].append(pnt)

    new_centroid = []

    # update the centroids of each cluster
    for lst in groups:
        # update the centroid
        new_centroid.append(upd_centroid(lst))
    return new_centroid


# Perform 10 iterations of k-means algorithm
for i in range(10):
    centroids = k_means(points, centroids)
    print('Centroids after ' + str(i + 1) + 'th iteration: ', centroids)