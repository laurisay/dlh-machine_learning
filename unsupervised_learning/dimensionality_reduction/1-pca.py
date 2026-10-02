#!/usr/bin/env python3
"""Module that performs PCA on a dataset."""
import numpy as np


def pca(X, ndim):
    """
    Perform PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where n is the number of
            data points and d is the number of dimensions in each
            point.
        ndim: The new dimensionality of the transformed X.

    Returns:
        T: numpy.ndarray of shape (n, ndim) containing the
            transformed version of X.
    """
    X_mean = X - np.mean(X, axis=0)

    U, S, Vh = np.linalg.svd(X_mean)

    W = Vh.T[:, :ndim]

    T = np.matmul(X_mean, W)

    return T
