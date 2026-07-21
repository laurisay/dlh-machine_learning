#!/usr/bin/env python3
"""Binomial distribution module."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize a Binomial distribution.

        Args:
            data (list): List of data to estimate the distribution
            n (int): Number of Bernoulli trials
            p (float): Probability of a "success"
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            
            # Calcul de la moyenne et de la variance
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            
            # Calcul de p avec la méthode des moments
            # Pour une distribution binomiale: p = 1 - (variance / mean)
            self.p = 1 - (variance / mean)
            
            # Calcul de n avec la méthode des moments
            # n = mean / p
            self.n = round(mean / self.p)
            
            # Recalcul de p avec le nouveau n
            self.p = mean / self.n
