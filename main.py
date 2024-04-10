import requests
from timeit import timeit
import sys
from api_alpha_vintage import * 
from api_eodhd import *
from evaluators import *
from api_finhub import *
from api_fmp import *
from helpers import *
from pandas_datareader_api import *

sys.path.insert(0, '/api_functions/')


fmp_key = "wpy0OAHOmFPLDyGbZzZ9IQuBlPMGf6v3"
aplha_vantage_key = "P0FAXOA7EI26OK9C"
tingo_key = "ef8c1728f6f1409157ab6a4f1266dd7af5df1ad5"
yfinance_api = " "
iex_key = "pk_5b65eb8e38e744f0b90e312a5c638d1b"
eodhd_key = "660734df8f7450.97003170"
fin_hub_key = "co3jcjpr01qj6vn80uogco3jcjpr01qj6vn80up0"
finage_key = "API_KEY01UJ76AC66CG8HPDTMJ75CW2GWR8FY0A"

prova_import()
prova_imported_2()

api_list = pd.Series(["Financial  Modelling Prep", "Alpha Vantage", "Quandl", "Tingo",
                      "YFinance", "IEX Cloud", "EODHD" ,"FinHub", "Finage", "Market Stack", "Poligon.io"
                    ])


time_response(prova_import)


comparison_df = pd.DataFrame(index = api_list)
comparison_df["Last update of a quote price"] = " "
comparison_df["Longest daily timeserie available"] = 8
comparison_df["Minimum time frequency available"] = dt.datetime(2010,1,1)
comparison_df["Nan values in a timeserie"] = 0
comparison_df["Deviation from the average values in a timeserie"] = 0
comparison_df["Time delay of the request"] = 0
comparison_df["Minimum time frequency available"] = 0

print(comparison_df)





"""
iterations = 100
total_time = timeit("print(30)", number=iterations, globals=globals())

average_time = total_time / iterations
print(average_time)

"""