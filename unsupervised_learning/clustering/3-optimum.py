#!/usr/bin/env python3
"""Module that tests for the optimum number of clusters by variance."""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    Test for the optimum number of clusters by variance.

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set.
        kmin: Positive integer containing the minimum number of
            clusters to check for (inclusive).
        kmax: Positive integer containing the maximum number of
            clusters to check for (inclusive).
        iterations: Positive integer containing the maximum number of
            iterations for K-means.

    Returns:
        results, d_vars: results is a list containing the outputs of
            K-means for each cluster size, and d_vars is a list
            containing the difference in variance from the smallest
            cluster size for each cluster size.
        None, None: On failure.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None

    if kmax is None:
        kmax = X.shape[0]

    if not isinstance(kmax, int) or kmax <= 0:
        return None, None
    if kmin >= kmax:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    results = []
    variances = []

    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        results.append((C, clss))
        variances.append(variance(X, C))

    d_vars = [variances[0] - var for var in variances]

    return results, d_vars
