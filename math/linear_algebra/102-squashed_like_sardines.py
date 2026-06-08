#!/usr/bin/env python3
"""Module to concatenate two matrices along a specific axis."""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specific axis.

    Args:
        mat1: first matrix (list of lists of any depth)
        mat2: second matrix (list of lists of any depth)
        axis: axis along which to concatenate

    Returns:
        New matrix concatenated, or None if cannot concatenate
    """
    # Helper function to get shape of matrix
    def get_shape(matrix):
        shape = []
        current = matrix
        while isinstance(current, list):
            shape.append(len(current))
            current = current[0] if current else None
        return shape

    # Helper function to check if shapes are compatible for concatenation
    def check_compatible(shape1, shape2, axis):
        if len(shape1) != len(shape2):
            return False
        for i in range(len(shape1)):
            if i != axis and shape1[i] != shape2[i]:
                return False
        return True

    # Helper function to create deep copy
    def deep_copy(matrix):
        if not isinstance(matrix, list):
            return matrix
        return [deep_copy(item) for item in matrix]

    # Get shapes
    shape1 = get_shape(mat1)
    shape2 = get_shape(mat2)

    # Check if concatenation is possible
    if not check_compatible(shape1, shape2, axis):
        return None

    # Recursive concatenation
    def recursive_cat(m1, m2, current_axis, target_axis):
        if current_axis == target_axis:
            # Concatenate at this level
            return deep_copy(m1) + deep_copy(m2)
        else:
            # Go deeper
            if not isinstance(m1, list) or not isinstance(m2, list):
                return None
            if len(m1) != len(m2):
                return None

            result = []
            for i in range(len(m1)):
                sub_result = recursive_cat(m1[i], m2[i], current_axis + 1, target_axis)
                if sub_result is None:
                    return None
                result.append(sub_result)
            return result

    return recursive_cat(mat1, mat2, 0, axis)
