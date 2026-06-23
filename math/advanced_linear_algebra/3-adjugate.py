#!/usr/bin/env python3
"""Module that calculates the adjugate matrix of a matrix."""


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
                matrix[row][:col]
                + matrix[row][col + 1:]
            )
            minor.append(minor_row)

        det += (
            ((-1) ** col)
            * matrix[0][col]
            * determinant(minor)
        )

    return det


def adjugate(matrix):
    """
    Calculates the adjugate matrix of a matrix.

    Args:
        matrix (list of lists): Matrix whose adjugate
        should be calculated.

    Returns:
        list of lists: Adjugate matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cofactor_matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            submatrix = []

            for r in range(n):
                if r != i:
                    submatrix.append(
                        matrix[r][:j]
                        + matrix[r][j + 1:]
                    )

            value = determinant(submatrix)
            value *= (-1) ** (i + j)

            row.append(value)

        cofactor_matrix.append(row)

    adj = []

    for j in range(n):
        row = []

        for i in range(n):
            row.append(cofactor_matrix[i][j])

        adj.append(row)

    return adj
