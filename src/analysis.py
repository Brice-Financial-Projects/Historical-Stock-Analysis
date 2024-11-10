"""src / analysis.py."""

import pandas as pd

def calculate_daily_returns(df):
    df['daily_return'] = df['close'].pct_change()
    return df

def moving_average(df, window=50):
    df[f'{window}_day_ma'] = df['close'].rolling(window=window).mean()
    return df
