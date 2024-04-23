
import requests
import datetime as dt
from datetime import datetime 
import pandas as pd

poligon_key = "yrLQ1dm3ZAujvqGds3ZBQq4zaE7X0R9a"

def latest_price_poligonio(ticker):
    """Get latest quote of a given ticker

    Args:
        ticker (strg): desired ticker. It can be stock, index of anything in a financial market.

    Returns:
        json object: data of the quote (current price, high, low...)
    """
    
    response = requests.get(
    f'''https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={poligon_key}''')
    
    data = response.json()
    
    return data

