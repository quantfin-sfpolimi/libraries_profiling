
import requests
import datetime as dt
from datetime import datetime 
import pandas as pd

tingo_key = "ef8c1728f6f1409157ab6a4f1266dd7af5df1ad5"


def latest_price_tingo(ticker):
    """
    Args:
        ticker (string): ticker of the selected stock

    Returns:
        float: current price of the selected stock
        float: delay (seconds) between now and the moment the stock price was registered
    """
    
    response = requests.get(
    f'https://api.tiingo.com/tiingo/daily/{ticker}/prices',
    headers={
        
        'Authorization' : "Token "+tingo_key,
        }
    )
    
    data = response.json()[0]
    price = data["adjClose"]
    
    timestamp_price = datetime.timestamp(datetime.strptime(data["date"],"%Y-%m-%dT%H:%M:%S%f%z"))    
    delay = datetime.timestamp(datetime.now()) - timestamp_price
    
    return  price, delay

def historical_price_tingo(ticker):
    """

    Args:
        ticker (string): ticker of the selected stock

    Returns:
        dataframe: dataframe with index datetime values and 1 column with adjusted closed price.
    """
    end_date = datetime.today().strftime("%Y-%m-%d")
    
    response = requests.get(
        f'https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate=1000-1-1&endDate={end_date}',
        headers={
        
        'Authorization' : "Token "+tingo_key,
        }
    )
    
    data = response.json()
    df = pd.DataFrame(data)
    df["date"] =  (pd.to_datetime(df["date"]))
    df.set_index(df["date"], inplace= True)
    
    
    return df["close"]

