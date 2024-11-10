"""src / analysis.py."""

import pandas as pd

def calculate_daily_returns(df):
    """
    Calculate the daily returns of the stock based on closing prices.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the stock data, with a 'close' column representing 
        daily closing prices.
        
    Returns
    -------
    pd.DataFrame
        The original DataFrame with an added 'daily_return' column that represents
        the percentage change in closing price from the previous day.
    """
    df['daily_return'] = df['close'].pct_change()
    return df


def moving_average(df, window=50):
    """
    Calculate the moving average of closing prices over a specified window.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the stock data, with a 'close' column representing 
        daily closing prices.
    window : int, optional
        The number of days over which to calculate the moving average, by default 50.
        
    Returns
    -------
    pd.DataFrame
        The original DataFrame with an added column named '{window}_day_ma', which
        represents the moving average of closing prices over the specified window.
        
    Notes
    -----
    The moving average is a rolling mean calculated on the 'close' column. The new 
    column is named based on the window size, such as '50_day_ma' for a 50-day 
    moving average.
    """
    df[f'{window}_day_ma'] = df['close'].rolling(window=window).mean()
    return df

