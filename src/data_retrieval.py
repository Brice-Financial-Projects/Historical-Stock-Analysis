"""src / data_retrieval.py."""

import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetch historical stock data for a given symbol from the Tiingo API.
    
    Parameters:
    -----------
    symbol : str
        The stock symbol (ticker) to retrieve data for (e.g., "AAPL").
    start_date : str
        The start date for the data in the format 'YYYY-MM-DD'.
    end_date : str
        The end date for the data in the format 'YYYY-MM-DD'.
        
    Returns:
    --------
    pd.DataFrame or None
        A DataFrame containing the historical stock data if successful, 
        otherwise None if there is an error in the API request.
        
    Notes:
    ------
    This function uses the `requests` library to fetch data and the `pandas` 
    library to store the returned data as a DataFrame. If the request fails, 
    None is returned instead of a DataFrame.
    """
    api_key = os.getenv("TIINGO_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set TIINGO_API_KEY in your .env file.")

    url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices?token={api_key}"
    headers = {"Content-Type": "application/json"}
    params = {
        "startDate": start_date,
        "endDate": end_date
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx

        data = response.json()
        return pd.DataFrame(data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
