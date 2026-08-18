#!/usr/bin/env python3
"""Function to compute descriptive statistics."""

import pandas as pd


def analyze(df):
    """Computes descriptive statistics for all columns except Timestamp.

    Args:
        df: pd.DataFrame to analyze.

    Returns:
        pd.DataFrame: descriptive statistics.
    """
    return df.drop(columns=['Timestamp']).describe()
