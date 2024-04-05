from helpers import *
import requests
from timeit import timeit

fmp_key = "wpy0OAHOmFPLDyGbZzZ9IQuBlPMGf6v3"
aplha_vantage_key = "P0FAXOA7EI26OK9C"
tingo_key = "ef8c1728f6f1409157ab6a4f1266dd7af5df1ad5"
yfinance_api = " "
iex_key = "pk_5b65eb8e38e744f0b90e312a5c638d1b"
eodhd_key = "660734df8f7450.97003170"
fin_hub_key = "co3jcjpr01qj6vn80uogco3jcjpr01qj6vn80up0"
finage_key = "API_KEY01UJ76AC66CG8HPDTMJ75CW2GWR8FY0A"



api_list = pd.Series(["Financial  Modelling Prep", "Alpha Vantage", "Quandl", "Tingo",
                      "YFinance", "IEX Cloud", "EODHD" ,"FinHub", "Finage"
                    ])


comparison_df = pd.DataFrame(index = api_list)
comparison_df["Minimum Time Frame"] = " "
comparison_df["Time Delay"] = 8
comparison_df["Longest-running timeserie"] = dt.datetime(2010,1,1)
comparison_df["Nan Value Rate"] = 0
comparison_df["Error Rate"] = 0
comparison_df["Max Free Calls"] = 0

print(comparison_df)





"""
iterations = 100
total_time = timeit("print(30)", number=iterations, globals=globals())

average_time = total_time / iterations
print(average_time)

"""