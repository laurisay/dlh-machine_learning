#!/usr/bin/env python3
"""Module that calculates the total intra-cluster variance for a dataset."""
import numpy as np


def variance(X, C):
    """
    Calculate the total intra-cluster variance for a data set.

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set.
        C: numpy.ndarray of shape (k, d) containing the centroid means
            for each cluster.

    Returns:
        var: The total variance, or None on failure.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None
    if not isinstance(C, np.ndarray) or len(C.shape) != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None

    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    min_distances = np.min(distances, axis=1)
    var = np.sum(min_distances ** 2)

    return var
