#!/usr/bin/env python3
"""Function to fill missing values in DataFrame."""


def fill(df):
    """Fills missing values in DataFrame according to specifications.

    Args:
        df: pd.DataFrame to fill.

    Returns:
        pd.DataFrame: modified DataFrame with filled values.
    """
    df = df.drop(columns=['Weighted_Price'])

    df['Close'] = df['Close'].fillna(method='ffill')

    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    return df
