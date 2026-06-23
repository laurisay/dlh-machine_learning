#!/usr/bin/env python3
"""Module that calculates the determinant of a matrix."""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): Matrix whose determinant is calculated.

    Returns:
        int or float: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Special case: 0x0 matrix
    if matrix == [[]]:
        return 1

    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # 2x2 matrix
    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for col in range(n):
        minor = []

        for row in range(1, n):
            minor_row = (
                matrix[row][:col] +
                matrix[row][col + 1:]
            )
            minor.append(minor_row)

        det += (
            ((-1) ** col)
            * matrix[0][col]
            * determinant(minor)
        )

    return det
