import numpy as np

actual = np.array(list(map(int, input().split())))
predicted = np.array(list(map(int, input().split())))


def accuracy_metric(actual, predicted):
    accuracy = 0
    # YOUR CODE GOES HERE
    matched_count = 0
    n = len(predicted)
    for i in range(n):
        if actual[i] == predicted[i]:
            matched_count += 1
    accuracy = matched_count / n * 100

    return accuracy
