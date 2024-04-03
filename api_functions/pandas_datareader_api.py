import pandas_datareader as pdr
import pandas_datareader.data as web
from pandas_datareader import data as pdr_data
import pandas as pd
import datetime as dt

import yfinance as yf
yf.pdr_override()

#DOCUMENTATION OF PANDAS DATAREADER
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

fmp_key = "wpy0OAHOmFPLDyGbZzZ9IQuBlPMGf6v3"
aplha_vantage_key = "P0FAXOA7EI26OK9C"
tingo_key = "ef8c1728f6f1409157ab6a4f1266dd7af5df1ad5"
yfinance_api = " "
quandl_key = "wcDkrxrYudTfwmW17yvF"
iex_key = "pk_5b65eb8e38e744f0b90e312a5c638d1b"
eodhd_key = "660734df8f7450.97003170"
fin_hub_key = "co3jcjpr01qj6vn80uogco3jcjpr01qj6vn80up0"
finage_key = "API_KEY01UJ76AC66CG8HPDTMJ75CW2GWR8FY0A"

stock = "AAPL"
start = dt.datetime(2010,1,1)
end = dt.date.today()

#TINGO
def tingo_df(ticker, start, end, key):
    dataframe = pdr.tiingo.TiingoDailyReader(ticker,start, end, api_key = key).read()
    return dataframe

#IEX CLOUD
def iex_pandas_data_reader(ticker, start, end, key):
    dataframe = pdr.iex.daily.IEXDailyReader(ticker, start, end, api_key = key).read()
    return dataframe

#ALPHA VANTAGE
def alpha_vantage_pandas_data_reader(ticker, start, end, key):
    dataframe = pdr.av.time_series.AVTimeSeriesReader(ticker, function='TIME_SERIES_DAILY',
                                                         start=start, end=end, 
                                                         api_key=key).read()
    return dataframe

#QUANDL
def quandl_pandas_datareader(ticker, start, end, key):
    dataframe =  pdr.quandl.QuandlReader(ticker, start=start, end=end,
                                    api_key=key).read()
    return dataframe

#STOOQ
def stooq_pandas_data_reader(ticker, start, end, key = None):
    dataframe = pdr.stooq.StooqDailyReader(ticker, start=start, end=end).read()
    return dataframe

#YAHOO FINANCE
def yahoo_finance_pandas_data_reader(ticker, start, end, key = None):
    dataframe = pdr_data.get_data_yahoo(ticker, start, end)
    #used different name for pdf to solve integer /int problem with yfinance
    return dataframe
