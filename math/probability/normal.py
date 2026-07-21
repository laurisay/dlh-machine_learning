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

        Args:
            x (float): The x-value

        Returns:
            float: The CDF value for x
        """
        # Calcul du z-score
        z = (x - self.mean) / self.stddev
        # Approximation de la CDF de la normale standard
        return 0.5 * (1 + self._erf(z / (2 ** 0.5)))

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.
        """
        z = (x - self.mean) / self.stddev
        return self._std_normal_cdf(z)

    def _std_normal_cdf(self, z):
        """
        Calcule la CDF de la distribution normale standard.
        """
        # Constantes pour l'approximation de Abramowitz et Stegun
        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429
        p = 0.3275911
        e = 2.7182818285

        # Sauvegarde du signe
        sign = 1
        if z < 0:
            sign = -1
            z = abs(z)

        # Approximation de la fonction d'erreur (erf)
        t = 1.0 / (1.0 + p * z)
        erf = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * (e ** (-z * z))
        erf *= sign

        # CDF = 0.5 * (1 + erf(z / sqrt(2)))
        return 0.5 * (1 + erf)
