#!/usr/bin/env python3
"""Mean and covariance module."""

import numpy as np


def mean_cov(X):
    """Calculates the mean and covariance of a dataset."""

    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    n = X.shape[0]

    mean = np.mean(X, axis=0, keepdims=True)

    X_centered = X - mean

    cov = np.dot(X_centered.T, X_centered) / (n - 1)

    return mean, cov
