#this api has its official python library
import finnhub
import datetime as dt
from datetime import datetime 

finhub_key = "co3jcjpr01qj6vn80uogco3jcjpr01qj6vn80up0"

def latest_price_finhub(ticker):
    """Get latest quote of a given ticker

    Args:
        ticker (strg): desired ticker. It can be stock, index of anything in a financial market.

    Returns:
        json object: data of the quote (current price, high, low...)
    """
    
    finnhub_client = finnhub.Client(api_key=finhub_key)
    data = finnhub_client.quote(ticker)
    return data

