#!/usr/bin/env python3
"""Marginal probability module."""

import numpy as np

intersection = __import__('1-intersection').intersection


def marginal(x, n, P, Pr):
    """Calculates the marginal probability of obtaining the data."""

    return np.sum(intersection(x, n, P, Pr))
