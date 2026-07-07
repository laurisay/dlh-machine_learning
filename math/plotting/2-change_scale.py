#!/usr/bin/env python3
"""
2-change_scale module

This module contains a function to plot exponential decay
of C-14 on a logarithmic scale.
"""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plots exponential decay of C-14 with logarithmic y-scale.
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # Plot x vs y as a line graph
    plt.plot(x, y)
    
    # Set labels and title
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of C-14')
    
    # Set y-axis to logarithmic scale
    plt.yscale('log')
    
    # Set x-axis range from 0 to 28650
    plt.xlim(0, 28650)
    
    plt.show()
