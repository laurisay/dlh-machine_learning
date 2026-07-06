#!/usr/bin/env python3

def summation_i_squared(n):
    """
    Calculates the sum of squares from 1 to n:
    Σ(i^2) for i = 1 to n
    
    Args:
        n: stopping condition (integer)
    
    Returns:
        integer value of the sum, or None if n is not valid
    """
    # Check if n is a valid integer and greater than or equal to 1
    if not isinstance(n, int) or n < 1:
        return None
    
    # Formula: n(n+1)(2n+1)/6
    result = n * (n + 1) * (2 * n + 1) // 6
    
    return result
