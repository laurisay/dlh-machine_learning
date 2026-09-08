#!/usr/bin/env python3
"""Module that calculates the expectation step in the EM algorithm."""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    Calculate the expectation step in the EM algorithm for a GMM.

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set.
        pi: numpy.ndarray of shape (k,) containing the priors for each
            cluster.
        m: numpy.ndarray of shape (k, d) containing the centroid means
            for each cluster.
        S: numpy.ndarray of shape (k, d, d) containing the covariance
            matrices for each cluster.

    Returns:
        g, l: g is a numpy.ndarray of shape (k, n) containing the
            posterior probabilities for each data point in each
            cluster, and l is the total log likelihood.
        None, None: On failure.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(pi, np.ndarray) or len(pi.shape) != 1:
        return None, None
    if not isinstance(m, np.ndarray) or len(m.shape) != 2:
        return None, None
    if not isinstance(S, np.ndarray) or len(S.shape) != 3:
        return None, None
    if not np.isclose(np.sum(pi), 1):
        return None, None
    if X.shape[1] != m.shape[1] or m.shape[1] != S.shape[1]:
        return None, None
    if pi.shape[0] != m.shape[0] or m.shape[0] != S.shape[0]:
        return None, None
    if S.shape[1] != S.shape[2]:
        return None, None

    k = pi.shape[0]
    n, d = X.shape

    P = np.zeros((k, n))

    for i in range(k):
        P[i] = pi[i] * pdf(X, m[i], S[i])

    total = np.sum(P, axis=0)
    g = P / total

    likelihood = np.sum(np.log(total))

    return g, likelihood
