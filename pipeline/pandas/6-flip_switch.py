#!/usr/bin/env python3
"""Function to flip and switch DataFrame."""


def flip_switch(df):
    """Sorts data in reverse chronological order and transposes it.

    Args:
        df: pd.DataFrame to transform.

    Returns:
        pd.DataFrame: transformed DataFrame with reversed order and transposed.
    """
    return df.sort_index(ascending=False).T
