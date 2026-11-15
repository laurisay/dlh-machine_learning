#!/usr/bin/env python3
"""Updates the learning rate using inverse time decay"""

import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    Updates the learning rate using inverse time decay in numpy

    alpha: the original learning rate
    decay_rate: weight used to determine the rate at which alpha decays
    global_step: number of passes of gradient descent that have elapsed
    decay_step: number of passes of gradient descent that should occur
        before alpha is decayed further

    The decay occurs in a stepwise fashion

    Returns the updated value for alpha
    """
    return alpha / (1 + decay_rate * np.floor(global_step / decay_step))
