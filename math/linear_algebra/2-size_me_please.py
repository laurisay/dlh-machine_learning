#!/usr/bin/env python3
"""Module to calculate the shape of a matrix."""

def matrix_shape(matrix):
    """Calculate the shape of a matrix."""
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        current = current[0] if len(current) > 0 else None
    return shape
