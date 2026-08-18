#!/usr/bin/env python3
"""Function to slice DataFrame by selecting specific columns and every 60th row."""

import pandas as pd


def slice(df):
    """Extracts High, Low, Close, Volume_(BTC) columns and selects every 60th row.

    Args:
        df: pd.DataFrame to slice.

    Returns:
        pd.DataFrame: sliced DataFrame with specified columns and rows.
    """
    return df.loc[::60, ['High', 'Low', 'Close', 'Volume_(BTC)']]
