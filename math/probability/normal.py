#!/usr/bin/env python3
"""Normal distribution module."""

import math


class Normal:
    """Represents a normal distribution."""

    # ... tes autres méthodes ...

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value.
        """
        pi = 3.1415926536
        e = 2.7182818285

        coefficient = 1 / (
            self.stddev * ((2 * pi) ** 0.5)
        )

        exponent = -(
            (x - self.mean) ** 2
        ) / (2 * (self.stddev ** 2))

        return coefficient * (e ** exponent)

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.
        """
        return 0.5 * (
            1 + math.erf(
                (x - self.mean) /
                (self.stddev * math.sqrt(2))
            )
        )
