# Historical Stock Analysis

This project retrieves, analyzes, and visualizes historical stock data using the Tiingo API. **Please note:** Tiingo's terms specify that their API is for personal or internal use only. To comply with these terms, this project does not distribute data retrieved from Tiingo, and users must obtain their own API keys to run the project.

## Project Objectives

- Retrieve historical stock price data.
- Calculate daily returns and moving averages.
- Visualize stock price trends over time.

## Getting Started

### 1. Obtain a Tiingo API Key

To use this project, you will need a Tiingo API key:

- Visit [Tiingo's API page](https://api.tiingo.com/) and sign up for an account.
- Once registered, navigate to the API section of your account and generate an API key.
- Keep this key private and do not share it, as it is tied to your account.

### 2. Project Setup

1. **Clone the Repository**:
    git clone [https://github.com/yourusername/historical-stock-analysis.git](https://github.com/yourusername/historical-stock-analysis.git)
    cd historical-stock-analysis

2. **Set Up a Conda Environment**:
    conda create --name stock_analysis python=3.8
    conda activate stock_analysis

3. **Install Requirements and Necessary Libraries by Running**:
    conda env create -f environment.yml

4. **Configure the API Key**:
    - In the main script (main.py), add your Tiingo API key to the API_KEY variable. This key is needed to retrieve data from Tiingo.

    - Example:
        API_KEY = "your_tiingo_api_key"

### 3. Usage

1. **Run the Project**:
    With your Tiingo API key configured, run the project using:
        python main.py

2. **Explore the Analysis**:
    The script will retrieve stock data, calculate daily returns and moving averages, and visualize the trends.

## Disclaimer

This project is intended for personal or educational use only. Please ensure compliance with Tiingo's Terms of Use, particularly if adapting this code for external projects.

## License

This project is licensed under the MIT License. See LICENSE for more details.
