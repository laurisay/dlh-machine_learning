#!/usr/bin/env python3
"""Normal distribution module."""


class Normal:
    """Represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize a Normal distribution.

        Args:
            data (list): List of data to estimate the distribution
            mean (float): Mean of the distribution
            stddev (float): Standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calcul de la moyenne
            self.mean = float(sum(data) / len(data))
            # Calcul de l'écart type (population)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)
