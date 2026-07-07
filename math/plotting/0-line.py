#!/usr/bin/env python3
"""
0-line module

This module contains a function to plot a cubic line graph
showing y = x^3 as a solid red line from x=0 to x=10.
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots y = x^3 as a solid red line from x=0 to x=10.
    """
    y = np.arange(0, 11) ** 3
    x = np.arange(0, 11)
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y, color='red')
    plt.xlim(0, 10)
    plt.show()
