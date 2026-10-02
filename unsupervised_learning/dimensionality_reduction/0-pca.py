#!/usr/bin/env python3
"""Module that performs PCA on a dataset."""
import numpy as np


def pca(X, var=0.95):
    """
    Perform PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where n is the number of
            data points and d is the number of dimensions in each
            point. All dimensions have a mean of 0 across all data
            points.
        var: The fraction of the variance that the PCA transformation
            should maintain.

    Returns:
        W: numpy.ndarray of shape (d, nd) containing the weights
            matrix that maintains var fraction of X's original
            variance, where nd is the new dimensionality of the
            transformed X.
    """
    U, S, Vh = np.linalg.svd(X)

    cumulative_variance = np.cumsum(S) / np.sum(S)

    nd = np.argwhere(cumulative_variance >= var)[0, 0] + 1

    W = Vh.T[:, :nd]

    return W
