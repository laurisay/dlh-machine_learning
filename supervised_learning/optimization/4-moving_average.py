#!/usr/bin/env python3
"""Calculates the weighted moving average of a data set"""


def moving_average(data, beta):
    """
    Calculates the weighted moving average of a data set

    data: list of data to calculate the moving average of
    beta: weight used for the moving average

    Uses bias correction

    Returns a list containing the moving averages of data
    """
    v = 0
    averages = []
    for i in range(len(data)):
        v = beta * v + (1 - beta) * data[i]
        averages.append(v / (1 - beta ** (i + 1)))
    return averages
