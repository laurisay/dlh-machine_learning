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

            self.mean = float(sum(data) / len(data))

            variance = sum(
                (x - self.mean) ** 2 for x in data
            ) / len(data)

            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.
        """
        return self.mean + (z * self.stddev)

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
        pi = 3.1415926536
        e = 2.7182818285

        z = (x - self.mean) / self.stddev

        if z < 0:
            return 0.5 * (
                1 - (
                    1 - (
                        1 / (1 + 0.2316419 * (-z))
                    ) * (
                        0.319381530 * (
                            e ** (-z ** 2 / 2)
                        )
                    )
                )
            )

        return 0.5 * (
            1 + (
                1 - (
                    1 / (1 + 0.2316419 * z)
                ) * (
                    0.319381530 * (
                        e ** (-z ** 2 / 2)
                    )
                )
            )
        )
