import requests
import datetime as dt
from datetime import datetime 
import pandas as pd

eodhd_key = "660734df8f7450.97003170"


def latest_price_tingo(ticker):
    """
    Args:
        ticker (string): ticker of the selected stock

    Returns:
        float: current price of the selected stock
        float: delay (seconds) between now and the moment the stock price was registered
    """
    
    response = requests.get(
    f'https://eodhd.com/api/real-time/{ticker}?api_token={eodhd_key}&fmt=json'

    )
    data = response.json()
    return data

def historical_price_tingo(ticker):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    end_date = datetime.today().strftime("%Y-%m-%d")
    
    response = requests.get(
        f'https://eodhd.com/api/eod/{ticker}?api_token={eodhd_key}&fmt=json'
        
    )
    
    data = response.json()
    if data is not None:
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])
        df.set_index(df["date"], inplace = True)
        return df["close"]
    return None

def historical_intraday_tingo(ticker, frequency= False):
    """

    Args:
        ticker (string): _description_
        frequency (string): time frequency of the price. values: ["1min","5min" "15min", "30min", "1hour", "4hour"]

    Returns:
        pandas dataframe: dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
        none if the data is not available with the free plan.
    """
    response = requests.get(
        f'https://eodhd.com/api/intraday/{ticker}?&interval={ticker}api_token={eodhd_key}&fmt=json'
    )
    try:
        data = response.url()
    except:
        return None
    return data    
    
def prova_import():
    print("Prova Import")
    
    
print(historical_price_tingo("AAPL"))