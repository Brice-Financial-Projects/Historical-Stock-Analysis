"""Main.py."""

from src.data_retrieval import fetch_stock_data
from src.analysis import calculate_daily_returns, moving_average
from src.visualization import plot_stock_data

# Configuration Constants
API_KEY = "YOUR_TIINGO_API_KEY"
SYMBOL = "AAPL"
START_DATE = "2020-01-01"
END_DATE = "2023-01-01"

def main():
    """
    Main function to execute the stock data pipeline:
    1. Fetch historical stock data.
    2. Calculate daily returns and moving averages.
    3. Visualize stock price data with moving averages.

    Steps
    -----
    - Fetches data using `fetch_stock_data`.
    - Analyzes data by calculating daily returns and moving averages.
    - Visualizes the analyzed data using `plot_stock_data`.

    Returns
    -------
    None
    """
    # Step 1: Fetch Data
    data = fetch_stock_data(symbol=SYMBOL, start_date=START_DATE,
                            end_date=END_DATE)
    if data is None:
        print("Failed to retrieve data.")
        return

    # Step 2: Analyze Data
    data = calculate_daily_returns(data)
    data = moving_average(data, window=50)
    data = moving_average(data, window=200)

    # Step 3: Visualize Data
    plot_stock_data(data, SYMBOL)

# Entry point for the script
if __name__ == "__main__":
    main()
