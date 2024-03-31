import time
import requests
from helpers import *
import pandas as pd


    



prova = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=demo")

response = requests.get(
  "https://financialmodelingprep.com/api/v3/search?query=AA",
  headers={"Authorization" : "<api_key_here>"}
)

data = prova.json()

df = pd.DataFrame(data["Time Series (Daily)"])
df = df.transpose()