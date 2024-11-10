"""Main.py."""

from src.data_retrieval import fetch_stock_data
from src.analysis import calculate_daily_returns, moving_average
from src.visualization import plot_stock_data

API_KEY = "YOUR_TIINGO_API_KEY"
SYMBOL = "AAPL"
START_DATE = "2020-01-01"
END_DATE = "2023-01-01"

def main():
    # Step 1: Fetch Data
    data = fetch_stock_data(SYMBOL, START_DATE, END_DATE, API_KEY)
    if data is None:
        print("Failed to retrieve data.")
        return

    # Step 2: Analyze Data
    data = calculate_daily_returns(data)
    data = moving_average(data, window=50)
    data = moving_average(data, window=200)

    # Step 3: Visualize Data
    plot_stock_data(data, SYMBOL)

if __name__ == "__main__":
    main()
