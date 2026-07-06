#!/usr/bin/env python3
"""
poly_derivative module

This module provides a function to calculate the derivative
of a polynomial represented as a list of coefficients.
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly: list of coefficients representing a polynomial
              where index represents the power of x

    Returns:
        new list of coefficients representing the derivative,
        [0] if derivative is 0,
        None if poly is not valid
    """
    # Check if poly is a valid list
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    # Check if all elements are numbers (int or float)
    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    # Calculate derivative
    derivative = []

    # Start from index 1 (skip constant term)
    for i in range(1, len(poly)):
        derivative.append(poly[i] * i)

    # If derivative is empty or all coefficients are 0
    if len(derivative) == 0 or all(coeff == 0 for coeff in derivative):
        return [0]

    return derivative
