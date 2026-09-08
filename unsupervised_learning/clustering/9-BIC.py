#!/usr/bin/env python3
"""Module that finds the best number of clusters for a GMM using BIC."""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """
    Find the best number of clusters for a GMM using the Bayesian
    Information Criterion.

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set.
        kmin: Positive integer containing the minimum number of
            clusters to check for (inclusive).
        kmax: Positive integer containing the maximum number of
            clusters to check for (inclusive). If None, set to the
            maximum number of clusters possible.
        iterations: Positive integer containing the maximum number of
            iterations for the EM algorithm.
        tol: Non-negative float containing the tolerance for the EM
            algorithm.
        verbose: Boolean that determines if the EM algorithm should
            print information to the standard output.

    Returns:
        best_k, best_result, l, b: best_k is the best value for k
            based on its BIC, best_result is a tuple containing
            (pi, m, S) for the best number of clusters, l is a
            numpy.ndarray of shape (kmax - kmin + 1) containing the
            log likelihood for each cluster size tested, and b is a
            numpy.ndarray of shape (kmax - kmin + 1) containing the
            BIC value for each cluster size tested.
        None, None, None, None: On failure.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None, None, None

    if kmax is None:
        kmax = X.shape[0]

    if not isinstance(kmax, int) or kmax <= 0:
        return None, None, None, None
    if kmin >= kmax:
        return None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None

    n, d = X.shape

    ks = range(kmin, kmax + 1)
    num_k = len(ks)

    log_likelihoods = np.zeros(num_k)
    bics = np.zeros(num_k)
    results = []

    for idx, k in enumerate(ks):
        pi, m, S, g, likelihood = expectation_maximization(
            X, k, iterations, tol, verbose)

        results.append((pi, m, S))
        log_likelihoods[idx] = likelihood

        p = (k * d) + (k * d * (d + 1) / 2) + (k - 1)
        bics[idx] = p * np.log(n) - 2 * likelihood

    best_idx = np.argmin(bics)
    best_k = ks[best_idx]
    best_result = results[best_idx]

    return best_k, best_result, log_likelihoods, bics
