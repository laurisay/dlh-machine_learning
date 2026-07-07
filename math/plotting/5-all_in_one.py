#!/usr/bin/env python3
"""
5-all_in_one module

This module contains a function to plot all 5 previous graphs
in one figure with a 3x2 grid layout.
"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """
    Plots all 5 previous graphs in one figure with 3x2 grid layout.
    """
    # Data for all plots
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # Create figure with 3x2 grid
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle('All in One')

    # Plot 1: Line Graph (0-line)
    ax1 = plt.subplot(3, 2, 1)
    ax1.plot(y0, color='red')
    ax1.set_xlim(0, 10)
    ax1.set_xlabel('x', fontsize='x-small')
    ax1.set_ylabel('y', fontsize='x-small')
    ax1.set_title('Line Graph', fontsize='x-small')

    # Plot 2: Scatter (1-scatter)
    ax2 = plt.subplot(3, 2, 2)
    ax2.scatter(x1, y1, color='magenta')
    ax2.set_xlabel('Height (in)', fontsize='x-small')
    ax2.set_ylabel('Weight (lbs)', fontsize='x-small')
    ax2.set_title('Scatter', fontsize='x-small')

    # Plot 3: Change of Scale (2-change_scale)
    ax3 = plt.subplot(3, 2, 3)
    ax3.plot(x2, y2)
    ax3.set_xlabel('Time (years)', fontsize='x-small')
    ax3.set_ylabel('Fraction Remaining', fontsize='x-small')
    ax3.set_title('Change of Scale', fontsize='x-small')
    ax3.set_yscale('log')
    ax3.set_xlim(0, 28650)

    # Plot 4: Two is better than one (3-two)
    ax4 = plt.subplot(3, 2, 4)
    ax4.plot(x3, y31, 'r--', label='C-14')
    ax4.plot(x3, y32, 'g-', label='Ra-226')
    ax4.set_xlabel('Time (years)', fontsize='x-small')
    ax4.set_ylabel('Fraction Remaining', fontsize='x-small')
    ax4.set_title('Two is better than one', fontsize='x-small')
    ax4.set_xlim(0, 20000)
    ax4.set_ylim(0, 1)
    ax4.legend(loc='upper right', fontsize='x-small')

    # Plot 5: Frequency (4-frequency) - takes 2 columns (positions 5 and 6)
    ax5 = plt.subplot(3, 2, (5, 6))
    ax5.hist(student_grades, bins=10, edgecolor='black')
    ax5.set_xlabel('Grades', fontsize='x-small')
    ax5.set_ylabel('Number of Students', fontsize='x-small')
    ax5.set_title('Frequency', fontsize='x-small')
    ax5.set_xlim(0, 100)
    ax5.set_xticks(np.arange(0, 101, 10))

    plt.tight_layout()
    plt.show()
