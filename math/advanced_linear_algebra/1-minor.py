#!/usr/bin/env python3
"""Module that calculates the minor matrix of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix."""
    if matrix == [[]]:
        return 1

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

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


def minor(matrix):
    """
    Calculates the minor matrix of a matrix.

    Args:
        matrix (list of lists): Matrix whose minor matrix is calculated.

    Returns:
        list of lists: Minor matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            submatrix = []

            for r in range(n):
                if r != i:
                    submatrix.append(
                        matrix[r][:j] + matrix[r][j + 1:]
                    )

            row.append(determinant(submatrix))

        result.append(row)

    return result
