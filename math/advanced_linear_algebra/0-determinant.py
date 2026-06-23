#!/usr/bin/env python3

def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): The matrix whose determinant should be calculated.

    Returns:
        int/float: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check for empty matrix
    if len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    
    # Check if all rows have the same length (square matrix)
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")
    
    # Base case: 0x0 matrix (represented as [[]])
    if n == 1 and len(matrix[0]) == 0:
        return 1
    
    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]
    
    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case: n x n matrix (n > 2)
    det = 0
    for j in range(n):
        # Create submatrix by removing row 0 and column j
        submatrix = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            submatrix.append(row)
        
        # Calculate cofactor and add to determinant
        cofactor = matrix[0][j] * determinant(submatrix)
        if j % 2 == 1:  # if column index is odd, subtract
            det -= cofactor
        else:           # if column index is even, add
            det += cofactor
    
    return det
