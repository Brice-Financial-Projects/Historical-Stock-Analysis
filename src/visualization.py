"""src / visualization.py."""

import matplotlib.pyplot as plt


def plot_stock_data(df, symbol):
    """
    Plot stock price data along with moving averages.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the stock data, with columns 'date', 'close',
        '50_day_ma', and '200_day_ma'.
    symbol : str
        The stock symbol (ticker) being plotted (e.g., "AAPL").
        
    Returns
    -------
    None
        This function displays a plot and does not return any value.
    
    Notes
    -----
    This function assumes the DataFrame contains pre-calculated columns
    for the 50-day and 200-day moving averages ('50_day_ma' and '200_day_ma').
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['close'], label='Close Price', linewidth=1.5)
    plt.plot(df['date'], df['50_day_ma'], label='50-Day MA', linestyle='--', linewidth=1.2)
    plt.plot(df['date'], df['200_day_ma'], label='200-Day MA', linestyle='--', linewidth=1.2)
    plt.title(f'{symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)  # Adds grid lines for better readability
    plt.tight_layout()  # Ensures labels and titles fit within the figure
    plt.show()
