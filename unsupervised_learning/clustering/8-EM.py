#!/usr/bin/env python3
"""Module that performs the expectation maximization for a GMM."""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    Perform the expectation maximization for a GMM.

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set.
        k: Positive integer containing the number of clusters.
        iterations: Positive integer containing the maximum number of
            iterations for the algorithm.
        tol: Non-negative float containing tolerance of the log
            likelihood, used to determine early stopping.
        verbose: Boolean that determines if information about the
            algorithm should be printed.

    Returns:
        pi, m, S, g, l: pi is a numpy.ndarray of shape (k,) containing
            the priors for each cluster, m is a numpy.ndarray of
            shape (k, d) containing the centroid means for each
            cluster, S is a numpy.ndarray of shape (k, d, d)
            containing the covariance matrices for each cluster, g is
            a numpy.ndarray of shape (k, n) containing the
            probabilities for each data point in each cluster, and l
            is the log likelihood of the model.
        None, None, None, None, None: On failure.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    if pi is None:
        return None, None, None, None, None

    g, likelihood = expectation(X, pi, m, S)
    if g is None:
        return None, None, None, None, None

    prev_likelihood = 0
    i = 0

    for i in range(iterations):
        if verbose and i % 10 == 0:
            print('Log Likelihood after {} iterations: {}'.format(
                i, round(likelihood, 5)))

        pi, m, S = maximization(X, g)
        g, likelihood = expectation(X, pi, m, S)

        if abs(likelihood - prev_likelihood) <= tol:
            break

        prev_likelihood = likelihood

    if verbose:
        print('Log Likelihood after {} iterations: {}'.format(
            i + 1, round(likelihood, 5)))

    return pi, m, S, g, likelihood
