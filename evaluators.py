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

def time_response(function_to_evaluate, stock = None, start = None, end = None, key = None):
    start_time = time.perf_counter()
    
    function_to_evaluate(stock)
    finish_time = time.perf_counter()
    
    return (finish_time - start_time)

def count_nan(dataframe_column):
    
    nan_values = dataframe_column.isna().sum()
    return nan_values

def get_longest_runnig(dataframe):
    first_day = dataframe.iloc[-1]
    last_day = dataframe.iloc[0]
    
    n_days = len(dataframe.index)
    return first_day, last_day, n_days
