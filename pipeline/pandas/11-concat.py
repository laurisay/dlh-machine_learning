#!/usr/bin/env python3
"""Function to concatenate two DataFrames."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Concatenates two DataFrames with specified conditions.

    Args:
        df1: pd.DataFrame (coinbase) to concatenate to.
        df2: pd.DataFrame (bitstamp) to select rows from.

    Returns:
        pd.DataFrame: concatenated DataFrame with keys.
    """
    df1 = index(df1)
    df2 = index(df2)

    df2_filtered = df2[df2.index <= 1417411920]

    return pd.concat([df2_filtered, df1], keys=['bitstamp', 'coinbase'])
