#!/usr/bin/env python3
"""Module to transpose a matrix."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    
    return transpose
