#!/usr/bin/env python3
"""Multivariate Normal distribution module."""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize the distribution."""

        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError(
                "data must be a 2D numpy.ndarray"
            )

        if data.shape[1] < 2:
            raise ValueError(
                "data must contain multiple data points"
            )

        n = data.shape[1]

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered = data - self.mean

        self.cov = np.dot(centered, centered.T) / (n - 1)
    def pdf(self, x):
        """Calculates the PDF at a data point."""

        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError(
                "x must have the shape ({}, 1)".format(d)
            )

        diff = x - self.mean

        inv_cov = np.linalg.inv(self.cov)

        exponent = -0.5 * np.matmul(
            np.matmul(diff.T, inv_cov),
            diff
        )

        denominator = np.sqrt(
            ((2 * np.pi) ** d) * np.linalg.det(self.cov)
        )

        return (np.exp(exponent) / denominator).item()
