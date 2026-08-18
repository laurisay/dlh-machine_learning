#!/usr/bin/env python3
"""Function to convert DataFrame columns to numpy array."""

import pandas as pd
import numpy as np


def array(df):
    """Selects last 10 rows of High and Close columns and converts to ndarray.

    Args:
        df: pd.DataFrame containing columns High and Close.

    Returns:
        np.ndarray: numpy array of the last 10 rows of High and Close.
    """
    return df[['High', 'Close']].tail(10).to_numpy()
