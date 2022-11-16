import numpy as np

point = [5,10,15]
X = [[4, 13, 2], [9, 8, 11], [14, 4, 2], [4, 12, 1], [2, 8, 3]]

query_point = np.array(point)
x_array = np.asarray(X)


def eucildeanDistance():
    # CALCULATE EUCLIDEAN DISTANCE
    euclid_distances = []
    for x_i in x_array:
        euclid_dist = np.round(np.sum((query_point - x_i) ** 2) ** 0.5, 2)
        # euclid_dist = dist(query_point, x_i)
        euclid_distances.append(euclid_dist)
    return np.array(euclid_distances)


def manhattanDistance():
    # CALCULATE MANHATTAN DISTANCE
    manhattan_distances = []
    for x_i in x_array:
        manhattan_dist = np.round(np.sum(np.absolute((query_point - x_i))), 2)
        manhattan_distances.append(manhattan_dist)
    return np.array(manhattan_distances)

print("eucildean --> ",eucildeanDistance())
print("manhattan --> ",manhattanDistance())