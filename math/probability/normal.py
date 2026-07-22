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

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.

        Args:
            x (float): The x-value

        Returns:
            float: The z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.

        Args:
            z (float): The z-score

        Returns:
            float: The x-value of z
        """
        return self.mean + (z * self.stddev)

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value.

        Args:
            x (float): The x-value

        Returns:
            float: The PDF value for x
        """
        # PDF normale: f(x) = 1/(σ√(2π)) * e^(-(x-μ)²/(2σ²))
        pi = 3.1415926536
        e = 2.7182818285
        coefficient = 1 / (self.stddev * ((2 * pi) ** 0.5))
        exponent = -((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        pdf_value = coefficient * (e ** exponent)
        return pdf_value

        def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.
        """
        z = (x - self.mean) / self.stddev

        if z < 0:
            return 1 - self.cdf(2 * self.mean - x)

        t = 1 / (1 + 0.2316419 * z)

        d = 0.3989423 * (
            2.718281828459045 ** (-(z ** 2) / 2)
        )

        probability = d * t * (
            0.3193815
            + t * (
                -0.3565638
                + t * (
                    1.781478
                    + t * (
                        -1.821256
                        + t * 1.330274
                    )
                )
            )
        )

        return 1 - probability
