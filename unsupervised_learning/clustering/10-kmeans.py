#!/usr/bin/env python3
"""Module that performs K-means on a dataset using sklearn."""
import sklearn.cluster


def kmeans(X, k):
    """
    Perform K-means on a dataset using sklearn.

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset.
        k: The number of clusters.

    Returns:
        C, clss: C is a numpy.ndarray of shape (k, d) containing the
            centroid means for each cluster, and clss is a
            numpy.ndarray of shape (n,) containing the index of the
            cluster in C that each data point belongs to.
    """
    model = sklearn.cluster.KMeans(n_clusters=k)
    model.fit(X)

    C = model.cluster_centers_
    clss = model.labels_

    return C, clss
