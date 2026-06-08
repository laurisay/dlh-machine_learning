#!/usr/bin/env python3
"""Module to slice a matrix along specific axes using list comprehensions."""


def np_slice(matrix, axes={}):
    """
    Slice a matrix along specific axes.

    Args:
        matrix: list to slice (can be nested lists)
        axes: dict where key is axis and value is tuple (start, stop, step)

    Returns:
        New list after applying all slices
    """
    def recursive_slice(data, depth, axes_dict, max_depth):
        """Recursively apply slices to nested lists."""
        if depth == max_depth:
            return data

        # Get the slice for current depth
        if depth in axes_dict:
            slice_params = axes_dict[depth]
            # Handle different slice parameter lengths
            if len(slice_params) == 1:
                start = slice_params[0]
                stop = None
                step = None
            elif len(slice_params) == 2:
                start, stop = slice_params
                step = None
            else:
                start, stop, step = slice_params[:3]

            # Apply slice to current level
            sliced = data[start:stop:step]
        else:
            sliced = data[:]  # Take everything

        # Recursively slice deeper levels
        if isinstance(sliced, list) and depth + 1 < max_depth:
            return [recursive_slice(item, depth + 1, axes_dict, max_depth)
                    for item in sliced]
        return sliced

    # Find the maximum depth of the matrix
    def get_depth(m):
        if not isinstance(m, list) or not m:
            return 0
        return 1 + get_depth(m[0])

    max_depth = get_depth(matrix)
    return recursive_slice(matrix, 0, axes, max_depth)
