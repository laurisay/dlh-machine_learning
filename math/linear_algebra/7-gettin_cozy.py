#!/usr/bin/env python3
"""Module to concatenate two 2D matrices along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis."""
    if axis == 0:
        # Vertical concatenation - same number of columns required
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Create a deep copy to avoid modifying original
        result = [row[:] for row in mat1]
        result.extend([row[:] for row in mat2])
        return result

    elif axis == 1:
        # Horizontal concatenation - same number of rows required
        if len(mat1) != len(mat2):
            return None
        # Create a deep copy and extend each row
        result = [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
        return result

    return None
