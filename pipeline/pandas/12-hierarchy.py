#!/usr/bin/env python3
"""Function to create hierarchical concatenation of two DataFrames."""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenates two DataFrames with hierarchical MultiIndex.

    Args:
        df1: pd.DataFrame (coinbase) to concatenate.
        df2: pd.DataFrame (bitstamp) to concatenate.

    Returns:
        pd.DataFrame: concatenated DataFrame with MultiIndex.
    """
    df1 = index(df1)
    df2 = index(df2)

    start = 1417411980
    end = 1417417980

    df1_filtered = df1[(df1.index >= start) & (df1.index <= end)]
    df2_filtered = df2[(df2.index >= start) & (df2.index <= end)]

    df_concat = pd.concat(
        [df2_filtered, df1_filtered],
        keys=['bitstamp', 'coinbase']
    )

    df_concat = df_concat.swaplevel(0, 1).sort_index(level=0)

    return df_concat
