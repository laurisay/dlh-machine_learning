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
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, int):
        return None

    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    integral = [C]

    for i in range(len(poly)):
        coeff = poly[i] / (i + 1)
        if isinstance(coeff, float) and coeff.is_integer():
            coeff = int(coeff)
        integral.append(coeff)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
