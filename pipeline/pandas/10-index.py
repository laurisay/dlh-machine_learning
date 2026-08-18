#!/usr/bin/env python3
"""Function to set Timestamp column as index."""


def index(df):
    """Sets Timestamp column as the index of the DataFrame.

    Args:
        df: pd.DataFrame containing a Timestamp column.

    Returns:
        pd.DataFrame: DataFrame with Timestamp as index.
    """
    return df.set_index('Timestamp')
