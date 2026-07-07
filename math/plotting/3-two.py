#!/usr/bin/env python3
"""
3-two module

This module contains a function to plot exponential decay
of two radioactive elements: C-14 and Ra-226.
"""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    Plots exponential decay of C-14 and Ra-226 on the same graph.
    """
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    # Plot y1 as dashed red line (C-14)
    plt.plot(x, y1, 'r--', label='C-14')
    
    # Plot y2 as solid green line (Ra-226)
    plt.plot(x, y2, 'g-', label='Ra-226')
    
    # Set labels and title
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')
    
    # Set axis ranges
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    
    # Add legend in upper right corner
    plt.legend(loc='upper right')
    
    plt.show()
