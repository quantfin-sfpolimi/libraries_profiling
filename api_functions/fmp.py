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
    
    price = response.json()[0]["price"]
    timestamp_price = response.json()[0]["timestamp"]

    delay = datetime.timestamp(datetime.now()) - timestamp_price
    return price, delay

def historical_price_fmp(ticker):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    response = requests.get(
        f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}',
         params=[("apikey",fmp_key)]
    )
    
    data = response.json()["historical"]
    if data is not None:
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])
        df.set_index(df["date"], inplace= True)
        df.drop("date", inplace= True, axis = 1)
        return df["adjClose"]
    return None

def historical_intraday_fmp(ticker, frequency):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    response = requests.get(
        f'https://financialmodelingprep.com/api/v3/historical-chart/{frequency}/{ticker}',
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
    


print(latest_price_fmp("AAPL"))

def count_nan(dataframe_column):
    
    nan_values = dataframe_column.isna().sum()
    return nan_values

def get_longest_runnig(dataframe):
    first_day = dataframe.iloc[-1]
    last_day = dataframe.iloc[0]
    
    n_days = len(dataframe.index)
    return first_day, last_day, n_days

