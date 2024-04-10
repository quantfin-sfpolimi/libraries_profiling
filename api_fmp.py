import requests
import datetime as dt
from datetime import datetime 
import pandas as pd
fmp_key = "wpy0OAHOmFPLDyGbZzZ9IQuBlPMGf6v3"

def latest_price_fmp(ticker):
    """
    Args:
        ticker (string): ticker of the selected stock

    Returns:
        float: current price of the selected stock
        float: delay (seconds) between now and the moment the stock price was registered
    """
    
    response = requests.get(
    "https://financialmodelingprep.com/api/v3/quote-order/"+ticker,
    params=[("apikey",fmp_key)]
    )
    
    data = response.json()
    
    return data

def historical_price_fmp(ticker, frequency = "1min",start ="2020-1-1", end="2024-2-2"):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    response = requests.get(
        f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start}&to={end}',
         params=[("apikey",fmp_key)]
    )
    
    data = response.json()
    return data

def historical_intraday_fmp(ticker, frequency,  start ="2020-1-1", end="2024-2-2"):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
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
    


print(historical_price_fmp("AAPL"))