#!/usr/bin/env python3
"""Converts a label vector into a one-hot matrix"""

import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    Converts a label vector into a one-hot matrix

    labels: vector of integer labels
    classes: number of classes (inferred from labels if None)

    Returns the one-hot matrix
    """
    return K.utils.to_categorical(labels, num_classes=classes)
