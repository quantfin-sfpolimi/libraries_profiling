import time
import pandas_datareader as pdr
import pandas_datareader.data as web
from pandas_datareader import data as pdr_data
import pandas as pd
import datetime as dt
import yfinance as yf
yf.pdr_override()


def prova_import():
    print("Imported!")

def time_response(api_function, stock, start, end):
    start_time = time.perf_counter()
    
    api_function(stock, start, end)
    finish_time = time.perf_counter()
    
    return finish_time - start_time

def count_nan(dataframe_column):
    
    nan_values = dataframe_column.isna().sum()
    return nan_values

def get_longest_runnig(dataframe):
    first_day = dataframe.iloc[-1]
    last_day = dataframe.iloc[0]
    
    n_days = len(dataframe.index)
    return first_day, last_day, n_days

