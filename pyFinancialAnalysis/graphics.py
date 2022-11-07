# Import libraries of Python
import pandas as pd
import numpy as np
import datetime
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
from tqdm import tqdm

# Import external libraries
import yfinance as yf

# Import our modules of Python
from informations import get_company_stock_information
from informations import find_index_date
from analysis import stock_growth
from analysis import stock_base_growth
from analysis import average_stock_growth
from analysis import average_stock_growth_base
from analysis import stock_standard_deviation
from analysis import stock_standard_deviation_base
from analysis import stock_variance
from analysis import stock_variance_base

def stock_price_graph_linear(stock_dataframe):
    """
    This function displays a linear graph about stock requested by the client.
    Also, it allows you to visualize the trend of the stock.
    """
    fig, ax = plt.subplots(figsize=(12,7), dpi = 90)
    plt.title("Time Serie Plot", size = "x-large", weight = "bold")
    plt.xlabel("Period", size = "large", weight = "semibold")
    plt.ylabel("Price", size = "large", weight="semibold")
    # Style of grid
    for i in ['bottom', 'left']:
        ax.spines[i].set_color('black')
    ax.spines[i].set_linewidth(1.5) 
    right_side = ax.spines["right"]
    right_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
    ax = plt.plot(stock_dataframe)
    plt.legend(stock_dataframe.columns)
    plt.show()

def stock_price_growth_graph(stock_dataframe):
    """
    
    """
    stock_dataframe_growth = stock_growth(stock_dataframe)
    fig, ax = plt.subplots(figsize = (12,7), dpi = 90)
    plt.title("Growth of Time Serie (%)", size = "x-large", weight = "bold")
    plt.xlabel("Period", size = "large", weight = "semibold")
    plt.ylabel("Growth (%)", size = "large", weight="semibold")
    # Style of grid
    for i in ['bottom', 'left']:
        ax.spines[i].set_color('black')
    ax.spines[i].set_linewidth(1.5) 
    right_side = ax.spines["right"]
    right_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
    ax = plt.plot(stock_dataframe_growth)
    plt.legend(stock_dataframe_growth.columns)
    plt.show()

def stock_price_growth_base_graph(stock_dataframe, dates):
    """
    
    """
    stock_dataframe_growth_base = stock_base_growth(stock_dataframe, dates)
    indexs = find_index_date(stock_dataframe, dates)
    label_base = str(stock_dataframe.index[indexs])[0:10]
    fig, ax = plt.subplots(figsize = (12,7), dpi = 90)
    plt.title(f'Growth base of Time Serie (%), Base: {label_base}', size = "x-large", weight = "bold")
    plt.xlabel("Period", size = "large", weight = "semibold")
    plt.ylabel("Growth (%)", size = "large", weight = "semibold")
    # Style of grid
    for i in ['bottom', 'left']:
        ax.spines[i].set_color('black')
    ax.spines[i].set_linewidth(1.5) 
    right_side = ax.spines["right"]
    right_side.set_visible(False)
    top_side = ax.spines["top"]
    top_side.set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
    ax = plt.plot(stock_dataframe_growth_base)
    plt.legend(stock_dataframe_growth_base.columns)
    plt.show()
    
def stock_chart_candlestick(ticker_name, start_time, end_time):
    """
    
    """
    stock_dataframe = yf.Ticker(ticker_name).history(start = start_time, end = end_time)[["Open", "High", "Low", "Close"]].reset_index()
    
    fig = go.Figure(data = [go.Candlestick(x = stock_dataframe["Date"],
                                           open = stock_dataframe["Open"],
                                           high = stock_dataframe["High"],
                                           low = stock_dataframe["Low"],
                                           close = stock_dataframe["Close"])])
    fig.update_layout(title = f'Candlestick Price History of {ticker_name}',
                      yaxis_title = f'{ticker_name} stock')
    
    fig.show()
    
def stock_average_growth_graph_bar(ticker_name, start_time, end_time, period_stock):
    stock_dataframe = get_company_stock_information(ticker_name, start_time, end_time, period_stock)
    stock_dataframe_growth = average_stock_growth(stock_dataframe)
    stock_dataframe_growth = stock_dataframe_growth.reset_index()
    stock_dataframe_growth = stock_dataframe_growth.rename(columns = {"index" : "Company"})
    stock_dataframe_growth = round(stock_dataframe_growth, 2)
    
    fig = px.bar(stock_dataframe_growth,
                 x = "Company",
                 y = "Stocks average growth",
                 text_auto = "2.0s",
                 color = "Company")
    fig.update_layout(title = "Average Stock Growth Bar Chart (%)")
    fig.show()

"""
How to use these function to make graphs?

"""