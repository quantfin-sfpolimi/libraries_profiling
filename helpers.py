# Libraries used 
import datetime as dt
import numpy as np
import os
import pandas as pd
import pickle
import yfinance as yf
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import History
from zlib import crc32

history = History()  # Ignore, it helps with model_data function

def pickle_dump(stocks_prices):
    """
    Pickles the given pandas DataFrame containing stock prices into a file named "stocks_prices_dataframe.pkl".

    Parameters:
        stocks_prices (pandas.DataFrame): DataFrame containing stock prices to be pickled.

    Returns:
        None
    """
    with open("stocks_prices_dataframe.pkl", "wb") as f:
        pickle.dump(stocks_prices, f)

def pickle_load(filename):
    """
    Unpickles and loads a pandas DataFrame from the specified file.

    Parameters:
        filename (str): Name of the file to unpickle.

    Returns:
        pandas.DataFrame: DataFrame containing the unpickled data.
    """
    with open(filename, "rb") as f:
        stocks_prices = pickle.load(f)
    return stocks_prices

def load_dataframe(years):
    """
    Loads stock price data either from a pickled file or downloads it online using the yfinance library.
    Returns a pandas DataFrame containing the stock prices and a list of tickers.

    Parameters:
        years (int): Number of years of historical data to load.

    Returns:
        Tuple[pandas.DataFrame, List[str]]: A tuple containing the pandas DataFrame of stock prices and a list of tickers.
    """
    if os.path.isfile("stocks_prices_dataframe.pkl"):
        stock_prices = pickle_load("stocks_prices_dataframe.pkl")
        tickers = stock_prices.columns.tolist()
    else:
        tickers = get_stockex_tickers()
        stock_prices = loaded_df(years=years, tickers=tickers)

    return stock_prices, tickers

def loaded_df(years, tickers):
    """
    Downloads stock price data for the specified number of years and tickers using yfinance.
    Returns a pandas DataFrame and pickles the data.

    Parameters:
        years (int): Number of years of historical data to load.
        tickers (List[str]): List of ticker symbols.

    Returns:
        pandas.DataFrame: DataFrame containing downloaded stock price data.
    """
    stocks_dict = {}
    time_window = 365 * years
    start_date = dt.datetime.now() - dt.timedelta(time_window)
    end_date = dt.datetime.now()
    for i, ticker in enumerate(tickers):
        print('Getting {} ({}/{})'.format(ticker, i, len(tickers)))
        prices = yf.download(ticker, start=start_date, end=end_date)
        stocks_dict[ticker] = prices['Adj Close']

    stocks_prices = pd.DataFrame.from_dict(stocks_dict)
    pickle_dump(stocks_prices=stocks_prices)
    return stocks_prices

def clean_df(percentage, tickers, stocks_prices):
    """
    Cleans the DataFrame by dropping stocks with NaN values exceeding the given percentage threshold.

    Parameters:
        percentage (float): Percentage threshold for NaN values.
        tickers (List[str]): List of ticker symbols.
        stocks_prices (pandas.DataFrame): DataFrame containing stock prices.

    Returns:
        pandas.DataFrame: Cleaned DataFrame.
    """
    if percentage > 1:
        percentage = percentage / 100
    for ticker in tickers:
        nan_values = stocks_prices[ticker].isnull().values.any()
        if nan_values:
            count_nan = stocks_prices[ticker].isnull().sum()
            if count_nan > (len(stocks_prices) * percentage):
                stocks_prices.drop(ticker, axis=1, inplace=True)
    return stocks_prices

