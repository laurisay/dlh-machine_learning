#!/usr/bin/env python3
"""Module to slice a matrix along specific axes."""


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
            params = axes[i]
            if len(params) == 1:
                slices.append(slice(params[0], None))
            elif len(params) == 2:
                slices.append(slice(params[0], params[1]))
            else:
                slices.append(slice(params[0], params[1], params[2]))
        else:
            slices.append(slice(None))

    return matrix[tuple(slices)]
