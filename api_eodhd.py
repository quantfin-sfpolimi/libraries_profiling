import requests
import datetime as dt
from datetime import datetime 
import pandas as pd

eodhd_key = "660734df8f7450.97003170"


def latest_price_eodhd(ticker):
    """Get latest quote of a given ticker

    Args:
        ticker (strg): desired ticker. It can be stock, index of anything in a financial market.

    Returns:
        json object: data of the quote (current price, high, low...)
    """
    
    response = requests.get(
    f'https://eodhd.com/api/real-time/{ticker}?api_token={eodhd_key}&fmt=json'

    )
    data = response.json()
    return data

def historical_price_eodhd(ticker):
    """Get historical data of a given ticker

    Args:
        ticker (strg): desider ticker

    Returns:
        pandas dataframe: dataframe containing all data available for free.
        None if the data is not available with the free plan.
    """
    
    
    response = requests.get(
        f'https://eodhd.com/api/eod/{ticker}?api_token={eodhd_key}&fmt=json'
        
    )
    
    data = response.json()
    if data is not None:
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])
        df.set_index(df["date"], inplace = True)
        return df
    return None

def historical_intraday_eodhd(ticker, frequency= False):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe containing all data available for free.
        None if the data is not available with the free plan.
    """
    response = requests.get(
        f'https://eodhd.com/api/intraday/{ticker}?interval={frequency}api_token={eodhd_key}&fmt=json'
    )
    data = response.json()
    if data is not None:
        df = pd.DataFrame(data)
        
        return df
    return None
    
    
    
print(historical_price_eodhd("AAPL"))