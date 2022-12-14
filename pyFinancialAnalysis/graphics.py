# Import libraries of Python
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
import scipy

import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from tqdm import tqdm

# Import external libraries
import yfinance as yf

# Import our modules of Python
from pyFinancialAnalysis.informations import get_company_stock_information
from pyFinancialAnalysis.informations import find_index_date
from pyFinancialAnalysis.analysis import stock_growth
from pyFinancialAnalysis.analysis import stock_base_growth
from pyFinancialAnalysis.analysis import average_stock_growth
from pyFinancialAnalysis.analysis import average_stock_growth_base
from pyFinancialAnalysis.analysis import stock_standard_deviation
from pyFinancialAnalysis.analysis import stock_standard_deviation_base
from pyFinancialAnalysis.analysis import stock_variance
from pyFinancialAnalysis.analysis import stock_variance_base

def stock_price_graph_linear(stock_dataframe):
    """
    This function displays a linear graph about stock requested by the client.
    Also, it allows you to visualize the trend of the stock.
    You can enter more than one ticker name in the dataframe, too.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_price_graph_linear(dataframe)
         
    Let's go!
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
    This function allows you to graph the growth of stock.
    Also, you can enter more than one ticker name in the dataframe.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_price_growth_graph(dataframe)
         
    Ready! 
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
    This function allows you to graph the base growth of stock.
    Also, you can enter more than one ticker name in the dataframe.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_price_growth_base_graph(dataframe, "2022-10-20")
         
    It's beautiful! 
    """
    try:
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
    except IndexError as e:
        print("The base date entered isn't in the range of the dataframe. \nPlease, enter another base date.")
        print("The base date may not be in the Yahoo Finance database.")
        print("Error is: ", e)
    except TypeError as te:
        print(te)
    
def stock_chart_candlestick(ticker_name, start_time, end_time):
    """
    This function allows you to graph chart candlestick.
    Also, you can enter just one ticker name.
    It's important that you enter the ticker name as a string and not in the list.
    e.g. stock_chart_candlestick("AAPL", "2022-01-01", "2022-10-30")
         
    It's amazing! 
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
    
    
def stock_average_growth_graph_bar(stock_dataframe):
    """
    This function allows you to graph bar of growth stocks.
    Also, you can put more than one ticker name in the dataframe.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_average_growth_graph_bar(dataframe, "2022-10-20")
         
    It's great!
    """
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
    

def stock_average_growth_base_graph_bar(stock_dataframe, dates):
    """
    This function allows you to graph bar of base growth stocks.
    Also, you can put more than one ticker name in the dataframe.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_average_growth_base_graph_bar(dataframe, "2022-10-20")
         
    Let's go!
    """
    try:
        stock_dataframe_growth_base = average_stock_growth_base(stock_dataframe, dates)
        stock_dataframe_growth_base = stock_dataframe_growth_base.reset_index()
        stock_dataframe_growth_base = stock_dataframe_growth_base.rename(columns = {"index" : "Company"})
        stock_dataframe_growth_base = round(stock_dataframe_growth_base, 2)
        
        fig = px.bar(stock_dataframe_growth_base,
                    x = "Company",
                    y = "Stocks average growth base",
                    text_auto = "2.0s", color = "Company")
        fig.update_layout(title = "Average Stock Growth Base Bar Chart (%)")
        fig.show()
    except TypeError as te:
        print("The key of value isn't exist in the dataframe.")
        print("Error: ", te)
    
def stock_standard_deviation_graph_bar(stock_dataframe):
    """
    This function allows you to graph bar the standard deviation of growth stocks.
    Also, you can put more than one ticker name in the dataframe.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_standard_deviation_graph_bar(dataframe)
         
    It's cool!
    """
    stock_dataframe_standard_deviation = stock_standard_deviation(stock_dataframe)
    stock_dataframe_standard_deviation = stock_dataframe_standard_deviation.reset_index()
    stock_dataframe_standard_deviation = stock_dataframe_standard_deviation.rename(columns = {"index" : "Company"})
    stock_dataframe_standard_deviation = round(stock_dataframe_standard_deviation, 2)
    
    fig = px.bar(stock_dataframe_standard_deviation, 
                 x = "Company",
                 y = "Stocks standard deviation",
                 text_auto = "2.0s",
                 color = "Company")
    fig.update_layout(title = "Standard Deviation of Stock Growth (%)")
    fig.show()
    
def stock_standard_deviation_base_graph_bar(stock_dataframe, dates):
    """
    This function allows you to graph bar the standard deviation of base growth stocks.
    Also, you cant put more than one ticker name in the dataframe.
    e.g. dataframe = get_company_stock_information(["AAPL", "AMZN"], "2022-01-01", "2022-10-30", "Close")
         stock_standard_deviation_graph_bar(dataframe, "2022-10-17")
         
    It's beautiful!
    """
    stock_dataframe_standard_deviation_base = stock_standard_deviation_base(stock_dataframe, dates)
    stock_dataframe_standard_deviation_base = stock_dataframe_standard_deviation_base.reset_index()
    stock_dataframe_standard_deviation_base = stock_dataframe_standard_deviation_base.rename(columns = {"index" : "Company"})
    stock_dataframe_standard_deviation_base = round(stock_dataframe_standard_deviation_base, 2)
    
    fig = px.bar(stock_dataframe_standard_deviation_base,
                x = "Company",
                y = "Stocks standard deviation",
                text_auto = "2.0s",
                color = "Company")
    fig.update_layout(title = "Standard Deviation of Stock Growth (%)")
    fig.show()

def stock_histogram(stock_ticker, start_time, end_time, period_stock):
    """
    This function allows you to graph histogram of stocks.
    Also, you can enter maximum of 5 ticker name and minimum of 1.
    e.g. stock_histogram(["AAPL", "AMZN", "TSLA"], "2022-01-01", "2022-10-30", "Close")
         
    It's amazing!
    """
    stock_dataframe = get_company_stock_information(stock_ticker, start_time, end_time, period_stock)
    name_columns = np.array(stock_dataframe.columns)
    if len(stock_ticker) == 1:
        x1 = np.array(stock_dataframe[name_columns[0]])
        hist_data = [x1]
        group_labels = stock_ticker
        fig = ff.create_distplot(hist_data, group_labels, bin_size = 2)
        fig.show()
    elif len(stock_ticker) == 2:
        x1 = np.array(stock_dataframe[name_columns[0]])
        x2 = np.array(stock_dataframe[name_columns[1]])
        hist_data = [x1, x2]
        group_labels = stock_ticker
        fig = ff.create_distplot(hist_data, group_labels, bin_size = 2)
        fig.show()
    elif len(stock_ticker) == 3:
        x1 = np.array(stock_dataframe[name_columns[0]])
        x2 = np.array(stock_dataframe[name_columns[1]])
        x3 = np.array(stock_dataframe[name_columns[2]])
        hist_data = [x1, x2, x3]
        group_labels = stock_ticker
        fig = ff.create_distplot(hist_data, group_labels, bin_size = 2)
        fig.show()
    elif len(stock_ticker) == 4:
        x1 = np.array(stock_dataframe[name_columns[0]])
        x2 = np.array(stock_dataframe[name_columns[1]])
        x3 = np.array(stock_dataframe[name_columns[2]])
        x4 = np.array(stock_dataframe[name_columns[3]])
        hist_data = [x1, x2, x3, x4]
        group_labels = stock_ticker
        fig = ff.create_distplot(hist_data, group_labels, bin_size = 2)
        fig.show()
    elif len(stock_ticker) == 5:
        x1 = np.array(stock_dataframe[name_columns[0]])
        x2 = np.array(stock_dataframe[name_columns[1]])
        x3 = np.array(stock_dataframe[name_columns[2]])
        x4 = np.array(stock_dataframe[name_columns[3]])
        x5 = np.array(stock_dataframe[name_columns[4]])
        group_labels = stock_ticker
        hist_data = [x1, x2, x3, x4, x5]
        fig = ff.create_distplot(hist_data, group_labels, bin_size = 2)
        fig.update_layout(title = "Histogram of stocks")
        fig.show()
    else:
        print("Introduce a maximum of 5 ticker names and a minimum of 1")
    
def stock_histplot(ticker_name, start_time, end_time, period_stock):
    """
    This function allows you to graph histplot of stocks.
    Also, you can enter n-ticker names, but it's necessary that you enter one ticker name.  
    e.g. stock_histplot(["AAPL", "AMZN", "TSLA"], "2022-01-01", "2022-10-30", "Close")
         
    That is great!
    """
    count = 1
    count_color = 0
    colors = ["orange", "blue", "red", "green", "black", "brown", "magenta","gray"]
    tickers_names = ticker_name
    
    for i in ticker_name:
        stock_dataframe = get_company_stock_information(ticker_name, start_time, end_time, period_stock).reset_index()
        stock_dataframe_columns = stock_dataframe.columns[count]
        fig, ax = plt.subplots(figsize = (12,8), dpi = 60)
        ax = sns.histplot(data = stock_dataframe,
                        x = stock_dataframe[stock_dataframe_columns],
                        kde = True,
                        color = colors[count_color])
        plt.title(f'Histplot of {tickers_names[count_color]} stock', size = 16)
        plt.ylabel("Count", size = 12)
        count_color += 1
        count += 1
        for i in ['bottom', 'left']:
            ax.spines[i].set_color('black')
            ax.spines[i].set_linewidth(1.5) 
        right_side = ax.spines["right"]
        right_side.set_visible(False)
        top_side = ax.spines["top"]
        top_side.set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        plt.show()