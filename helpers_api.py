import time
import requests
from helpers import *
import pandas as pd

def timer_api(url):
    start_time = time.perf_counter()
    
    response = requests.get(url)
    


prova = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=demo")

data = prova.json()

df = pd.DataFrame.from_records(data)
print(df)