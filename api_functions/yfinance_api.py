import yfinance as yf
import requests
import datetime as dt
from datetime import datetime 
import pandas as pd
from pandas_datareader import data as pdr
yf.pdr_override()


def latest_price_yfinance(ticker):
    """
    Args:
        ticker (string): ticker of the selected stock

    Returns:
        float: current price of the selected stock
        float: delay (seconds) between now and the moment the stock price was registered
    """
    
    data = yf.Ticker(ticker).history(period = "1min")
    price = data["Close"]
    timestamp_price = datetime.timestamp(data.index[0] )
    
    delay = datetime.timestamp(datetime.now()) - timestamp_price
    
    return price, delay

def historical_price_yfinance(ticker):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    end_date = datetime.today()
    start_date = datetime(1000,1,1)
    dataframe = pdr.get_data_yahoo(ticker,start_date,end_date)
    dataframe["close"] = dataframe["Adj Close"]
    
    return dataframe["close"]
    

def historical_intraday_yfinance(ticker, frequency=False):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    end_date = datetime.today()
    start_date = datetime(1000,1,1)
    dataframe = pdr.get_data_yahoo(ticker,start_date,end_date)
    dataframe["close"] = dataframe["Adj Close"]
    
    return dataframe["close"]
    
    
print(historical_intraday_yfinance("AAPL"))