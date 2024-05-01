import requests
import datetime as dt
from datetime import datetime 
import pandas as pd
fmp_key = "wpy0OAHOmFPLDyGbZzZ9IQuBlPMGf6v3"

def latest_price_fmp(ticker):
    """Get latest quote of a given ticker

    Args:
        ticker (strg): desired ticker. It can be stock, index of anything in a financial market.

    Returns:
        json object: data of the quote (current price, high, low...)
    """
    
    response = requests.get(
    "https://financialmodelingprep.com/api/v3/quote-order/"+ticker,
    params=[("apikey",fmp_key)]
    )
    
    data = response.json()
    
    return data

def historical_price_fmp(ticker,start ="1900-1-1", end="2024-2-2"):
    """Get historical data of a given ticker

    Args:
        ticker (string): desired ticker
        start (str, optional): start day. Defaults to "1900-1-1".
        end (str, optional): end day. Defaults to "2024-2-2".

    Returns:
        json obect: Json object with list of json object (one for each index)
    """
    response = requests.get(
        f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start}&to={end}',
         params=[("apikey",fmp_key)]
    )
    
    data = response.json()
    return data

def historical_intraday_fmp(ticker, frequency,  start ="2020-1-1", end="2024-2-2"):
    """Get historical data of a given ticker with the possibility to set different frequency.

    Args:
        ticker (str): desired ticker
        frequency (str): desired frequency. (1min, 5min, 15min, 30min, 1hour, 4hour)
        start (str, optional): start. Defaults to "2020-1-1".
        end (str, optional): end. Defaults to "2024-2-2".

    Returns:
        _type_: _description_
    """
    response = requests.get(
        f'https://financialmodelingprep.com/api/v3/historical-chart/{frequency}/{ticker}?from={start}&to={end}',
         params=[("apikey",fmp_key)]
    )
    
    data = response.json()
    if data is not None:
        
        df = pd.DataFrame(data)
        
        df["date"] = pd.to_datetime(df["date"])
        df.set_index(df["date"], inplace= True)
        df.drop("date", inplace= True, axis = 1)
        return df["close"]
    
    return None
    
print(historical_price_fmp("AAPL") )