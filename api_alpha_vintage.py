alpha_vantage_key = "P0FAXOA7EI26OK9C"
import requests
from datetime import datetime 
import pandas as pd

def latest_price_alpha_vantage(ticker):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        (float, float)): current price of the selected stock, 
        delay (seconds) between now and the moment the stock price was registered
    """
    
    response = requests.get(
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}',
        params=[("apikey", alpha_vantage_key)]
    )
    data = response.json()
    
    return data

def historical_price_alpha_vantage(ticker):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    response = requests.get(
        f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full',
        params=[("apikey",alpha_vantage_key)]
    )
    data = response.json()["Time Series (Daily)"]
    
    if data is not None:
        df = pd.DataFrame(data)
        df = df.transpose()
        df["close"] = df["4. close"]
        df.drop("4. close", inplace=True, axis = 1)
        return df
    return None   

def historical_intraday_alpha_vantage(ticker, frequency="1min", outputsize = "full"):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    response = requests.get(
        f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={frequency}&outputsize={outputsize}',
        params=[("apikey", alpha_vantage_key)]
    )
    data = response.json()["Time Series ("+frequency+")"]
    
    if data is not None:
        df = pd.DataFrame(data)
        df = df.transpose()
        df["close"] = df["4. close"]
        df.drop("4. close", inplace=True, axis = 1)
        return df
    return None
  