# Import libraries of Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


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

now = datetime.now()

def financial_dashboard(stock_dataframe, dates):
    """
    How to use this function?
    
    First, you need to create a dataframe.
    Using the función get_company_stock_information(ticker_name, start_time, end_time, period_stock).
    This function belongs the informations.py module.
    e.g. stock_dataframe = get_company_stock_information(["AAPL"], "2022-01-01", "2022-10-30", "Close")
    
    Then, you must call the variable, using the main function.
    e.g. financial_dashboard(stock_dataframe, "2022-10-10")
    
    Ready! 😋
    You will have your financial dashboard!
    This is great! 😎
    """
    try:
        stock_growth_base_dataframe = stock_base_growth(stock_dataframe, dates)
        stock_variance_dataframe = stock_variance(stock_dataframe)
        stock_standard_deviation_dataframe = stock_standard_deviation(stock_dataframe)
        
        fig = plt.figure(figsize = (20,12), dpi = 80)
        
        # Graph 1
        
        ax1 = plt.subplot2grid((3,3), (0,0), colspan= 3)
        ax1.plot(stock_dataframe, linestyle = "dashed", linewidth = 2)
        ax1.set_title("Historical Data Price")
        ax1.set_ylabel("Price ($)")
        ax1.legend(labels = stock_dataframe.columns)
        [ax1.axhline(i, color = "green", alpha = 0.4, linestyle = "dashed") for i in stock_dataframe.max().values]
        [ax1.axhline(i, color = "red", alpha = 0.4, linestyle = "dashed") for i in stock_dataframe.min().values]
        for i in ['bottom', 'left']:
            ax1.spines[i].set_color('black')
            ax1.spines[i].set_linewidth(1.2) 
        right_side = ax1.spines["right"]
        right_side.set_visible(False)
        top_side = ax1.spines["top"]
        top_side.set_visible(False)
        ax1.set_axisbelow(True)
        ax1.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        
        # Graph 2
        
        ax2 = plt.subplot2grid((3,3), (1,0), colspan= 2)
        ax2.plot(stock_growth_base_dataframe, linestyle = "dashed", linewidth = 1.5)
        ax2.set_title(f'Stock Base {dates} Growth (%)')
        ax2.set_ylabel("Growth (%)")
        ax2.legend(labels = stock_growth_base_dataframe.columns)
        for i in ['bottom', 'left']:
            ax2.spines[i].set_color('black')
            ax2.spines[i].set_linewidth(1.2) 
        right_side = ax2.spines["right"]
        right_side.set_visible(False)
        top_side = ax2.spines["top"]
        top_side.set_visible(False)
        ax2.set_axisbelow(True)
        ax2.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        
        # Graph 3
        
        ax3 = plt.subplot2grid((3,3), (1,2), rowspan = 2)
        ax3.bar(list(stock_standard_deviation_dataframe.index), 
                list((stock_standard_deviation_dataframe.values).flatten()),
                color = ["orange", "blue", "red", "green", "black", "brown", "magenta","gray"])
        ax3.set_title("Stock Standard Deviation")
        ax3.legend(labels = stock_standard_deviation_dataframe.columns)
        for i in ['bottom', 'left']:
            ax3.spines[i].set_color('black')
            ax3.spines[i].set_linewidth(1.2) 
        right_side = ax3.spines["right"]
        right_side.set_visible(False)
        top_side = ax3.spines["top"]
        top_side.set_visible(False)
        ax3.set_axisbelow(True)
        ax3.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        
        # Graph 4
        
        ax4 = plt.subplot2grid((3,3), (2,0))
        ax4.bar(list(stock_variance_dataframe.index), 
                list((stock_variance_dataframe.values).flatten()),
                color = ["orange", "blue", "red", "green", "black", "brown", "magenta","gray"])
        ax4.set_title("Stock Variance")
        ax4.legend(labels = stock_variance_dataframe.columns)
        for i in ['bottom', 'left']:
            ax4.spines[i].set_color('black')
            ax4.spines[i].set_linewidth(1.2) 
        right_side = ax4.spines["right"]
        right_side.set_visible(False)
        top_side = ax4.spines["top"]
        top_side.set_visible(False)
        ax4.set_axisbelow(True)
        ax4.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        
        # Graph 5
        
        ax5 = plt.subplot2grid((3,3), (2,1))
        ax5.hist(stock_dataframe.values, histtype= "step")
        ax5.set_title("Stocks Histogram Step")
        ax5.legend(labels = stock_dataframe.columns)
        for i in ['bottom', 'left']:
            ax5.spines[i].set_color('black')
            ax5.spines[i].set_linewidth(1.2) 
        right_side = ax5.spines["right"]
        right_side.set_visible(False)
        top_side = ax5.spines["top"]
        top_side.set_visible(False)
        ax5.set_axisbelow(True)
        ax5.grid(color='gray', linewidth=1, axis='y', alpha=0.4)
        
        plt.suptitle(f'Financial Analysis Dashboard\n{now.year}-{now.month}-{now.day}\n{now.hour}:{now.minute}:{now.second}\n', size = 18)
        plt.subplots_adjust(wspace=0.193, hspace=0.333, left=0.057, right=0.943, top=0.86, bottom=0.082)
        
        plt.show()
    
    except TypeError as te:
        print("The key of value isn't exist in the dataframe.")
        print("Error: ", te)
    
# if __name__ == "__main__":
#     stocks = get_company_stock_information(["AAPL", "AMZN"], "2021-01-01", "2022-10-30", period_stock="Close")
#     # print(stock_base_growth(stocks, "2022-10-17"))
#     financial_dashboard(stocks, "2022-10-17")