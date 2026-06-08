#!/usr/bin/env python3
"""Module to slice a numpy array along specific axes."""


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
            # Utiliser slice(*axes[i]) pour que Python interprète correctement
            # (2,) -> slice(2) -> stop=2
            # (1, 3) -> slice(1, 3) -> start=1, stop=3
            # (None, None, -2) -> slice(None, None, -2)
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None))

    return matrix[tuple(slices)]
