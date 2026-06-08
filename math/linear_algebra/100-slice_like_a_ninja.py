#!/usr/bin/env python3
"""Module to slice a numpy array along specific axes."""
import numpy as np


def np_slice(matrix, axes={}):
    """
    Slice a matrix along specific axes.

    Args:
        matrix: numpy.ndarray to slice
        axes: dict where key is axis and value is tuple (start, stop, step)

    Returns:
        New numpy.ndarray after applying all slices
    """
    slices = []
    for i in range(matrix.ndim):
        if i in axes:
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None))

    return matrix[tuple(slices)]
