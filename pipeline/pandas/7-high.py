#!/usr/bin/env python3
"""Function to sort DataFrame by High price in descending order."""


def high(df):
    """Sorts DataFrame by High price in descending order.

    Args:
        df: pd.DataFrame to sort.

    Returns:
        pd.DataFrame: sorted DataFrame by High price descending.
    """
    return df.sort_values(by='High', ascending=False)
