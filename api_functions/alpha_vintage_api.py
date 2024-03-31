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
        f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min',
        params=[("apikey", alpha_vantage_key)]
    )
    data = response.json()["Time Series (1min)"]
    latest = list(data)[0]
    price = data[latest]["4. close"]
    timestamp_price = datetime.timestamp(datetime.strptime(latest,"%Y-%m-%d %H:%M:%S"))    
    delay = datetime.timestamp(datetime.now()) - timestamp_price
    
    return price, delay

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
        return df["close"]
    return None   

def historical_intraday_alpha_vantage(ticker, frequency):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    response = requests.get(
        f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={frequency}',
        params=[("apikey", alpha_vantage_key)]
    )
    data = response.json()["Time Series ("+frequency+")"]
    
    if data is not None:
        df = pd.DataFrame(data)
        df = df.transpose()
        df["close"] = df["4. close"]
        df.drop("4. close", inplace=True, axis = 1)
        return df["close"]
    return None
  

print(latest_price_alpha_vantage_2("AAPL") )