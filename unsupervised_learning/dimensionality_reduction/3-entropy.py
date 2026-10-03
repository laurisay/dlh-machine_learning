#!/usr/bin/env python3
"""Module that calculates the Shannon entropy and P affinities."""
import numpy as np


def HP(Di, beta):
    """
    Calculate the Shannon entropy and P affinities relative to a data point.

    Args:
        Di: numpy.ndarray of shape (n - 1,) containing the pairwise
            distances between a data point and all other points.
        beta: numpy.ndarray of shape (1,) containing the beta value.

    Returns:
        (Hi, Pi): Hi is the Shannon entropy and Pi contains
        the P affinities.
    """
    P = np.exp(-Di * beta)
    sumP = np.sum(P)

    Hi = np.log2(sumP) + beta * np.sum(Di * P) / (
        sumP * np.log(2)
    )

    Pi = P / sumP

    return Hi, Pi
