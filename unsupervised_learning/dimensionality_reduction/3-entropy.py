#!/usr/bin/env python3
"""Module that calculates the Shannon entropy and P affinities."""
import numpy as np


def HP(Di, beta):
    """
    Calculate the Shannon entropy and P affinities relative to a
    data point.

    Args:
        Di: numpy.ndarray of shape (n - 1,) containing the pairwise
            distances between a data point and all other points
            except itself.
        beta: numpy.ndarray of shape (1,) containing the beta value
            for the Gaussian distribution.

    Returns:
        (Hi, Pi): Hi is the Shannon entropy of the points, and Pi is
            a numpy.ndarray of shape (n - 1,) containing the P
            affinities of the points.
    """
    P = np.exp(-Di * beta)
    sumP = np.sum(P)

    Hi = np.log(sumP) + beta * np.sum(Di * P) / sumP

    Pi = P / sumP

    return Hi, Pi
