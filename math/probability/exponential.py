#!/usr/bin/env python3
"""Exponential distribution module."""


class Exponential:
    """Represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize an Exponential distribution.

        Args:
            data (list): List of data to estimate the distribution
            lambtha (float): Expected number of occurrences in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Pour une distribution exponentielle, lambtha = 1 / moyenne
            self.lambtha = float(1 / (sum(data) / len(data)))
