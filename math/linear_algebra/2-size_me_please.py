#!/usr/bin/env python3

def matrix_shape(matrix):
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        current = current[0] if len(current) > 0 else None
    return shape
