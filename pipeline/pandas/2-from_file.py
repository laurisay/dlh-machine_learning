#!/usr/bin/env python3
"""Function to load data from a file into a pd.DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """Loads data from a file as a pd.DataFrame.

    Args:
        filename: str, name of the file to load from.
        delimiter: str, column separator.

    Returns:
        pd.DataFrame: loaded DataFrame.
    """
    return pd.read_csv(filename, delimiter=delimiter)
