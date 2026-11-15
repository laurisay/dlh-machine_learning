#!/usr/bin/env python3
"""Creates mini-batches for mini-batch gradient descent"""

shuffle_data = __import__('2-shuffle_data').shuffle_data


def create_mini_batches(X, Y, batch_size):
    """
    Creates mini-batches to be used for training a neural network
    using mini-batch gradient descent

    X: numpy.ndarray of shape (m, nx) representing input data
        m: number of data points
        nx: number of features in X
    Y: numpy.ndarray of shape (m, ny) representing the labels
        m: same number of data points as in X
        ny: number of classes for classification tasks
    batch_size: number of data points in a batch

    Returns a list of mini-batches containing tuples (X_batch, Y_batch)
    """
    m = X.shape[0]
    X_shuffled, Y_shuffled = shuffle_data(X, Y)

    mini_batches = []
    for start in range(0, m, batch_size):
        end = start + batch_size
        mini_batches.append((X_shuffled[start:end], Y_shuffled[start:end]))

    return mini_batches
