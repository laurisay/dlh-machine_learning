#!/usr/bin/env python3
"""Module to add two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Add two 2D matrices element-wise."""
    if len(mat1) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None

        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result
