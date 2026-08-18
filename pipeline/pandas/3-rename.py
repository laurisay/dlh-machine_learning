#!/usr/bin/env python3
"""Function to rename and convert Timestamp column."""

import pandas as pd


def rename(df):
    """Renames Timestamp column to Datetime, converts to datetime.

    Args:
        df: pd.DataFrame containing a column named Timestamp.

    Returns:
        pd.DataFrame with Datetime and Close columns.
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]
