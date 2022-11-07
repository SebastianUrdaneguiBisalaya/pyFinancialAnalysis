# Import libraries of Python

import pandas as pd
import numpy as np

# Import our own modules of Python

from informations import find_index_date

# Stock performance analysis

def stock_growth(stock_dataframe):
    stock_dataframe_growth = ((stock_dataframe - stock_dataframe.shift(1))/stock_dataframe.shift(1))*100
    return stock_dataframe_growth

def stock_base_growth(stock_dataframe, dates):
    indexs = find_index_date(stock_dataframe, dates)
    stock_dataframe_growth_base = (stock_dataframe/stock_dataframe.iloc[indexs])*100
    return stock_dataframe_growth_base

# Stock mean analysis

def average_stock_growth(stock_dataframe):
    stock_dataframe_average_growth = stock_growth(stock_dataframe)
    stock_dataframe_average_growth = pd.DataFrame(stock_dataframe_average_growth.mean())
    stock_dataframe_average_growth = stock_dataframe_average_growth.rename(columns = {0 : "Stocks average growth"})
    return stock_dataframe_average_growth

def average_stock_growth_base(stock_dataframe, dates):
    indexs = find_index_date(stock_dataframe, dates)
    







