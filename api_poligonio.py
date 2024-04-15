
import requests
import datetime as dt
from datetime import datetime 
import pandas as pd

poligon_key = "yrLQ1dm3ZAujvqGds3ZBQq4zaE7X0R9a"

def latest_price_poligonio(ticker):
    response = requests.get(
    f'''https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={poligon_key}''')
    
    data = response.json()
    
    return data

print(latest_price_poligonio("AAPL") )