#!/usr/bin/env python3
"""Module to add two matrices of any dimension."""


def add_matrices(mat1, mat2):
    """
    Add two matrices element-wise.

    Args:
        mat1: first matrix (list of lists of any depth)
        mat2: second matrix (list of lists of any depth)

    Returns:
        New matrix with element-wise sum, or None if shapes differ
    """
    # Check if both are lists and have the same length
    if isinstance(mat1, list) and isinstance(mat2, list):
        if len(mat1) != len(mat2):
            return None

        result = []
        for i in range(len(mat1)):
            # Recursively add sub-elements
            sub_result = add_matrices(mat1[i], mat2[i])
            if sub_result is None:
                return None
            result.append(sub_result)

        return result
    else:
        # Base case: both are numbers
        if isinstance(mat1, (int, float)) and isinstance(mat2, (int, float)):
            return mat1 + mat2
        return None
