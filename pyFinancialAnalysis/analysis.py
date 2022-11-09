# Import libraries of Python

import pandas as pd
import numpy as np

# Import our own modules of Python

from informations import find_index_date
from informations import get_company_stock_information

# Stock performance analysis

def stock_growth(stock_dataframe):
    stock_dataframe_growth = ((stock_dataframe - stock_dataframe.shift(1))/stock_dataframe.shift(1))*100
    stock_dataframe_growth = stock_dataframe_growth.dropna()
    return stock_dataframe_growth

def stock_base_growth(stock_dataframe, dates):
    indexs = find_index_date(stock_dataframe, dates)
    stock_dataframe_growth_base = (stock_dataframe/stock_dataframe.iloc[indexs])*100
    stock_dataframe_growth_base = stock_dataframe_growth_base.dropna()
    return stock_dataframe_growth_base

def average_stock_growth(stock_dataframe):
    stock_dataframe_average_growth = stock_growth(stock_dataframe)
    stock_dataframe_average_growth = pd.DataFrame(stock_dataframe_average_growth.mean())
    stock_dataframe_average_growth = stock_dataframe_average_growth.rename(columns = {0 : "Stocks average growth"})
    return stock_dataframe_average_growth

def average_stock_growth_base(stock_dataframe, dates):
    stock_dataframe_average_growth_base = stock_base_growth(stock_dataframe, dates)
    stock_dataframe_average_growth_base = pd.DataFrame(stock_dataframe_average_growth_base.mean())
    stock_dataframe_average_growth_base = stock_dataframe_average_growth_base.rename(columns = {0 : "Stocks average growth base"})
    return stock_dataframe_average_growth_base

# Stock standard deviation analysis

def stock_standard_deviation(stock_dataframe):
    stock_standard_deviation_dataframe = stock_growth(stock_dataframe)
    stock_standard_deviation_dataframe = pd.DataFrame(np.std(stock_standard_deviation_dataframe))
    stock_standard_deviation_dataframe = stock_standard_deviation_dataframe.rename(columns = {0 : "Stocks standard deviation"})
    return stock_standard_deviation_dataframe


def stock_standard_deviation_base(stock_dataframe, dates):
    try:
        stock_standard_deviation_base_dataframe = stock_base_growth(stock_dataframe, dates)
        stock_standard_deviation_base_dataframe = pd.DataFrame(np.std(stock_standard_deviation_base_dataframe))
        stock_standard_deviation_base_dataframe = stock_standard_deviation_base_dataframe.rename(columns = {0 : "Stocks standard deviation"})
        return stock_standard_deviation_base_dataframe
    except TypeError as te:
        print("The key of value isn't exist in the dataframe.")
        print("Error: ", te)
        
# Stock variance analysis

def stock_variance(stock_dataframe):
    stock_variance_dataframe = stock_growth(stock_dataframe)
    stock_variance_dataframe = pd.DataFrame(np.var(stock_variance_dataframe))
    stock_variance_dataframe = stock_variance_dataframe.rename(columns = {0 : "Stock growth variance"})
    return stock_variance_dataframe

def stock_variance_base(stock_dataframe, dates):
    try:
        stock_variance_base_dataframe = stock_base_growth(stock_dataframe, dates)
        stock_variance_base_dataframe = pd.DataFrame(np.var(stock_variance_base_dataframe))
        stock_variance_base_dataframe = stock_variance_base_dataframe.rename(columns = {0 : "Stock growth variance"})
        return stock_variance_base_dataframe
    except TypeError as te:
        print("The key of value isn't exist in the dataframe.")
        print("Error: ", te)


"""
How to use these functions?

First, you must create a dataframe with the information.py module, specifically using 
the function get_company_stock_information(ticker_name, start_time, end_time, period_stock)
with its respective parameters. Then, this information of dataframe you must store it in 
a variable with any name. 

e.g.  aapl_dataframe = get_company_stock_information(["AAPL"], start_time = "2022-10-01", end_time = "2022-10-30", period_stock = "Close")

Second, when you have created a variable with information of dataframe, you can use the functions
of this module. That easy!

e.g. How much is the daily return on Apple stock?

You must write the following lines of code in Google Colab (for example):
aapl_dataframe = get_company_stock_information(["AAPL"], start_time = "2022-10-01", end_time = "2022-10-30", period_stock = "Close")
aapl_performance_dataframe = stock_growth(aapl_dataframe)

Ready! That is all! No more.🤓
"""


