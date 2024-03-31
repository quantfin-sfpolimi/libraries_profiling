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
""" 
Tingo has some problems with data reader, in order to fix them update pandas datareader by tiping in the terminal:
pip install git+https://github.com/pydata/pandas-datareader.git
"""

tingo_df = pdr.tiingo.TiingoDailyReader(stock,start, end, api_key = tingo_key).read()

#IEX CLOUD
#function not working due to free plan (data available with upgraded premium plan)
#df_iex = pdr.iex.daily.IEXDailyReader(stock, start, end, api_key = iex_key).read()

#ALPHA VANTAGE
"""
df_alpha_vantage = pdr.av.time_series.AVTimeSeriesReader(stock, function='TIME_SERIES_DAILY',
                                                         start=start, end=end, 
                                                         api_key=aplha_vantage_key).read()
"""
#QUANDL
df_quandl = pdr.quandl.QuandlReader(stock, start=start, end=end,
                                    api_key=quandl_key).read()


#STOOQ
df_stooq = pdr.stooq.StooqDailyReader(stock, start=start, end=end).read()

#YAHOO FINANCE
df_yahoo = pdr_data.get_data_yahoo(stock, start, end)
#used different name for pdf to solve integer /int problem with yfinance
