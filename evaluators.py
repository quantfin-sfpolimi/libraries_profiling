import time
import pandas_datareader as pdr
import pandas_datareader.data as web
from pandas_datareader import data as pdr_data
import pandas as pd
import datetime as dt
import yfinance as yf
yf.pdr_override()

stock = "AAPL"
start = dt.datetime(1800,1,1)
end = dt.date.today()

def yahoo_finance_pandas_data_reader(ticker, start, end, key = None):
    dataframe = pdr_data.get_data_yahoo(ticker, start, end)
    #used different name for pdf to solve integer /int problem with yfinance
    return dataframe

def time_response(api_function, stock, start, end):
    start_time = time.perf_counter()
    
    api_function(stock, start, end)
    finish_time = time.perf_counter()
    
    return finish_time - start_time

print(time_response(yahoo_finance_pandas_data_reader, stock, start, end) )