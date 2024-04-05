#this api has its official python library
import finnhub
import datetime as dt
from datetime import datetime 

finhub_key = "co3jcjpr01qj6vn80uogco3jcjpr01qj6vn80up0"

def latest_price_finhub_1(ticker):
    finnhub_client = finnhub.Client(api_key=finhub_key)
    data = finnhub_client.quote(ticker)
    price = data["c"]
    timestamp_price = data["t"]
    
    delay = datetime.timestamp(datetime.now()) - timestamp_price

    return price,delay

 