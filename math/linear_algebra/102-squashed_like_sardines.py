#!/usr/bin/env python3
"""Module to concatenate two matrices along a specific axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis recursively."""
    def get_shape(m):
        """Return shape of matrix as list."""
        if not isinstance(m, list):
            return []
        return [len(m)] + get_shape(m[0])

    def check_shape(m1, m2, axis):
        """Check if matrices can be concatenated."""
        s1, s2 = get_shape(m1), get_shape(m2)
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if i != axis and s1[i] != s2[i]:
                return False
        return True

    def deep_copy(m):
        """Create deep copy of matrix."""
        if not isinstance(m, list):
            return m
        return [deep_copy(x) for x in m]

    def concat(m1, m2, depth):
        """Recursively concatenate matrices."""
        if depth == axis:
            return deep_copy(m1) + deep_copy(m2)

        if not isinstance(m1, list) or not isinstance(m2, list):
            return None
        if len(m1) != len(m2):
            return None

        result = []
        for a, b in zip(m1, m2):
            sub = concat(a, b, depth + 1)
            if sub is None:
                return None
            result.append(sub)
        return result

    if not check_shape(mat1, mat2, axis):
        return None

    return concat(mat1, mat2, 0)
