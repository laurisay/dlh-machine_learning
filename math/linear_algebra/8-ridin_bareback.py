#!/usr/bin/env python3
"""Module to multiply two matrices."""


def mat_mul(mat1, mat2):
    """Multiply two 2D matrices."""
    # Check if multiplication is possible
    if len(mat1[0]) != len(mat2):
        return None

    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    cols_mat2 = len(mat2[0])

    # Create result matrix filled with zeros
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    # Perform matrix multiplication
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
