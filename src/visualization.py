"""src / visualization.py."""

import matplotlib.pyplot as plt

def plot_stock_data(df, symbol):
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['close'], label='Close Price')
    plt.plot(df['date'], df['50_day_ma'], label='50-Day MA')
    plt.plot(df['date'], df['200_day_ma'], label='200-Day MA')
    plt.title(f'{symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
