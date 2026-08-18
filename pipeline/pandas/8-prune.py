#!/usr/bin/env python3
"""Function to remove rows where Close column has NaN values."""


def prune(df):
    """Removes rows where Close column has NaN values.

    Args:
        df: pd.DataFrame to prune.

    Returns:
        pd.DataFrame: DataFrame with rows containing NaN in Close removed.
    """
    return df.dropna(subset=['Close'])
