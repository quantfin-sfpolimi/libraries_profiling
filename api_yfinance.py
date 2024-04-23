import yfinance as yf
import requests
import datetime as dt
from datetime import datetime 
import numpy as np

import pandas as pd
from pandas_datareader import data as pdr

#yf.pdr_override()

def historical_price_yfinance(ticker, frequency = "1d", start = dt.date(1000,1,1), end = dt.datetime.today()):
    """Get historical data of a given ticker

    Args:
        ticker (str): desired ticker
        frequency (str, optional): frequency of data. Defaults to "1d". 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mos
            1min granularity is limited to 7 days.
            Frequency belows 1day are limited to 60 day
        start (datetime object, optional): start day. Defaults to dt.date(1000,1,1).
        end (datetime object, optional): end day. Defaults to dt.datetime.today().

    Returns:
        pandas dataframe: dataframe with all the data available
    """
    

    
    company = yf.Ticker(ticker)
    dataframe = company.history(interval = frequency, start = start, end = end)
    return dataframe

def latest_price_yfinance(ticker):
    """Get latest quote of a given ticker

    Args:
        ticker (strg): desired ticker. It can be stock, index of anything in a financial market.

    Returns:
        json object: data of the quote (current price, high, low...)
    """
    
    company = yf.Ticker("AAPL")
    return company.info


