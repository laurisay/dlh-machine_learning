#!/usr/bin/env python3
"""Module that calculates the Shannon entropy and P affinities."""
import numpy as np


def HP(Di, beta):
    """
    Calculate the Shannon entropy and P affinities.

    Args:
        Di: numpy.ndarray of shape (n - 1,) containing pairwise distances.
        beta: numpy.ndarray of shape (1,) containing beta.

    Returns:
        Hi: Shannon entropy.
        Pi: P affinities.
    """
    P = np.exp(-Di * beta)
    sumP = np.sum(P)

    Pi = P / sumP
    Hi = -np.sum(Pi * np.log2(Pi))

    return Hi, Pi
