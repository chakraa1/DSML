import numpy as np


def logloss(z, y_true, x):
    '''z, y_true and x are lists
       output -> Two numpy arrays are expected to be returned'''

    z = np.asarray(z)
    y_true = np.asarray(y_true)
    x = np.asarray(x)

    # YOUR CODE GOES HERE
    y_hat = 1 / (1 + np.exp(- (z)))
    logloss = -y_true * np.log(y_hat) - (1 - y_true) * np.log(1 - y_hat)
    grad = y_hat - y_true
    grad = grad * x[:, 0]

    return np.round(logloss, 2), np.round(grad, 2)