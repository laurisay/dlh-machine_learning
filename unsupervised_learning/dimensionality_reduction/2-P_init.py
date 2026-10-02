#!/usr/bin/env python3
"""Module that initializes variables for t-SNE."""
import numpy as np


def P_init(X, perplexity):
    """
    Initialize all variables required to calculate the P affinities
    in t-SNE.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset to be
            transformed by t-SNE.
        perplexity: The perplexity that all Gaussian distributions
            should have.

    Returns:
        (D, P, betas, H): D is a numpy.ndarray of shape (n, n)
            containing the squared pairwise distance between two data
            points (diagonal is 0), P is a numpy.ndarray of shape
            (n, n) initialized to all 0's, betas is a numpy.ndarray
            of shape (n, 1) initialized to all 1's, and H is the
            Shannon entropy for the given perplexity (base 2).
    """
    n, d = X.shape

    sum_X = np.sum(np.square(X), axis=1)

    D = np.add(np.add(-2 * np.matmul(X, X.T), sum_X).T, sum_X)
    np.fill_diagonal(D, 0)

    P = np.zeros((n, n))

    betas = np.ones((n, 1))

    H = np.log2(perplexity)

    return D, P, betas, H
