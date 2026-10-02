#!/usr/bin/env python3
"""Module that calculates the Q affinities."""
import numpy as np


def Q_affinities(Y):
    """
    Calculate the Q affinities.

    Args:
        Y: numpy.ndarray of shape (n, ndim) containing the low
            dimensional transformation of X.

    Returns:
        Q, num: Q is a numpy.ndarray of shape (n, n) containing the
            Q affinities, and num is a numpy.ndarray of shape (n, n)
            containing the numerator of the Q affinities.
    """
    n, ndim = Y.shape

    sum_Y = np.sum(np.square(Y), axis=1)

    D = np.add(np.add(-2 * np.matmul(Y, Y.T), sum_Y).T, sum_Y)
    np.fill_diagonal(D, 0)

    num = 1 / (1 + D)
    np.fill_diagonal(num, 0)

    Q = num / np.sum(num)

    return Q, num
