#!/usr/bin/env python3
"""
poly_integral module

This module provides a function to calculate the integral
of a polynomial represented as a list of coefficients.
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Args:
        poly: list of coefficients representing a polynomial
              where index represents the power of x
        C: integration constant (integer)

    Returns:
        new list of coefficients representing the integral,
        None if poly or C are not valid
    """
    # Check if poly is a valid list
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    # Check if C is an integer
    if not isinstance(C, int):
        return None

    # Check if all elements in poly are numbers (int or float)
    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    # Calculate integral
    integral = [C]  # Start with integration constant

    # For each coefficient at index i, divide by (i+1) and add to position (i+1)
    for i in range(len(poly)):
        coeff = poly[i] / (i + 1)
        # If coefficient is a whole number, convert to int
        if isinstance(coeff, float) and coeff.is_integer():
            coeff = int(coeff)
        integral.append(coeff)

    # Remove trailing zeros to make the list as small as possible
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    # If integral is [0] and C was 0, return [0]
    if len(integral) == 1 and integral[0] == 0:
        return [0]

    return integral
