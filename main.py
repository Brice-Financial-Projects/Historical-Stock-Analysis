"""Main.py."""

import os
from src.data_retrieval import fetch_stock_data
from src.analysis import calculate_daily_returns, moving_average
from src.visualization import plot_stock_data
from datetime import datetime
import pandas as pd


# Configuration Constants
API_KEY = "YOUR_TIINGO_API_KEY"  # Ensure your .env or environment variable is configured correctly
SYMBOL = "AAPL"
START_DATE = "2020-01-01"
END_DATE = "2024-10-31"

def save_data_to_csv(data, filename="data/historical_stock_data.csv"):
    """
    Save the stock data to a CSV file with a unique timestamped filename.

    Parameters:
        data (pd.DataFrame): The DataFrame containing stock data.
        filename (str): The base name of the file to save the data to.
    """
    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filename)
    timestamped_filename = f"{base}_{timestamp}{ext}"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(timestamped_filename), exist_ok=True)

    # Save the data to the timestamped filename
    data.to_csv(timestamped_filename, index=False)
    print(f"Data saved to {timestamped_filename}")


def main():
    """
    Main function to execute the stock data pipeline:
    1. Fetch historical stock data.
    2. Save the data to a CSV file.
    3. Calculate daily returns and moving averages.
    4. Visualize stock price data with moving averages.

    Steps
    -----
    - Fetches data using `fetch_stock_data`.
    - Saves data to CSV.
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

    # Step 2: Save Data to CSV
    save_data_to_csv(data, "data/historical_stock_data.csv")

    # Step 3: Analyze Data
    data = calculate_daily_returns(data)
    data = moving_average(data, window=50)
    data = moving_average(data, window=200)

    # Step 4: Visualize Data
    plot_stock_data(data, SYMBOL)

# Entry point for the script
if __name__ == "__main__":
    main()

