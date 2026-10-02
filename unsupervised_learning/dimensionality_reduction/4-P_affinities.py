#!/usr/bin/env python3
"""Module that calculates the symmetric P affinities of a dataset."""
import numpy as np
P_init = __import__('2-P_init').P_init
HP = __import__('3-entropy').HP


def P_affinities(X, tol=1e-5, perplexity=30.0):
    """
    Calculate the symmetric P affinities of a data set.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset to be
            transformed by t-SNE.
        tol: The maximum tolerance allowed (inclusive) for the
            difference in Shannon entropy from perplexity for all
            Gaussian distributions.
        perplexity: The perplexity that all Gaussian distributions
            should have.

    Returns:
        P: numpy.ndarray of shape (n, n) containing the symmetric P
            affinities.
    """
    n, d = X.shape

    D, P, betas, H = P_init(X, perplexity)

    for i in range(n):
        low = None
        high = None
        beta = betas[i].copy()

        Di = np.concatenate((D[i, :i], D[i, i + 1:]))

        Hi, Pi = HP(Di, beta)
        Hdiff = Hi - H

        while np.abs(Hdiff) > tol:
            if Hdiff > 0:
                low = beta[0]
                if high is None:
                    beta[0] *= 2
                else:
                    beta[0] = (beta[0] + high) / 2
            else:
                high = beta[0]
                if low is None:
                    beta[0] /= 2
                else:
                    beta[0] = (beta[0] + low) / 2

            Hi, Pi = HP(Di, beta)
            Hdiff = Hi - H

        P[i, :i] = Pi[:i]
        P[i, i + 1:] = Pi[i:]
        betas[i] = beta

    P = (P + P.T) / (2 * n)

    return P
