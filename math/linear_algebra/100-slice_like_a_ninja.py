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
    # Create a tuple of slices for each dimension
    slices = []
    for i in range(matrix.ndim):
        if i in axes:
            # Unpack the tuple to create a slice object
            slices.append(slice(*axes[i]))
        else:
            # No slice specified for this axis, take everything
            slices.append(slice(None))

    return matrix[tuple(slices)]
