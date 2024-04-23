alpha_vantage_key = "P0FAXOA7EI26OK9C"
import requests
from datetime import datetime 
import pandas as pd

def latest_price_alpha_vantage(ticker):
    """Get latest quote of a given ticker,

    Args:
        ticker (strg): desired ticker. It can be stock, index of anything in a financial market.

    Returns:
        json object: data of the quote (current price, high, low...)
    """
    
    response = requests.get(
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}',
        params=[("apikey", alpha_vantage_key)]
    )
    data = response.json()
    
    return data

def historical_price_alpha_vantage(ticker):
    """Get historical data of a given ticker

    Args:
        ticker (strg): desider ticker

    Returns:
        pandas dataframe: dataframe containing all data available for free.
        None if the data is not available with the free plan.
    """
    
    
    response = requests.get(
        f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full',
        params=[("apikey",alpha_vantage_key)]
    )
    data = response.json()["Time Series (Daily)"]
    
    if data is not None:
        df = pd.DataFrame(data)
        df = df.transpose()
        
        return df
    return None   

def historical_intraday_alpha_vantage(ticker, frequency="1min", outputsize = "full"):
    """_summary_

    Args:
        ticker (str): _description_
        frequency (str, optional): frequency of the data. Defaults to "1min". 1min, 5min, 15min, 30min, 60min are supported.
        outputsize (str, optional): _description_. Defaults to "full".

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
        None if the data is not available with the free plan.
    
    """
    response = requests.get(
        f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={frequency}&outputsize={outputsize}',
        params=[("apikey", alpha_vantage_key)]
    )
    data = response.json()["Time Series ("+frequency+")"]
    
    if data is not None:
        df = pd.DataFrame(data)
        df = df.transpose()
        
        return df
    return None
  