import pandas as pd

import yfinance as yf

def get_basic_information_company(ticker_name):
    stock = yf.Ticker(ticker_name)
    stock_info = stock.info
    serie_info = pd.Series(stock_info)
    return serie_info

# e.g. get_basic_information_company("AAPL")

def get_specific_information(ticker_name, options, date = None):
    stock = yf.Ticker(ticker_name)
    if options == 1:
        print(f'Major Holders of {ticker_name}')
        option_1_info = pd.DataFrame(stock.major_holders)
        option_1_info = option_1_info.rename(columns={0:"Percentage", 1:"% of Shares Held by"})
        return option_1_info
    elif options == 2:
        print(f'Institutional Holders of {ticker_name}')
        return stock.institutional_holders
    elif options == 3:
        print(f'Market Capitalization of {ticker_name}')
        option_3_info = stock.info["marketCap"]
        print(f'The market capitalization of company {ticker_name} is ${option_3_info}.')
    elif options == 4:
        print(f'Dividends of {ticker_name}')
        return pd.DataFrame(stock.dividends).reset_index()
    elif options == 5:
        try:
            print(f'Option Calls of {ticker_name}')
            return stock.option_chain(date).calls
        except ValueError as e:
            print("Introduce the date available in the format YYYY-MM-DD. \n", e)
    elif options == 6:
        try:
            print(f'Option Puts of {ticker_name}')
            return stock.option_chain(date).puts
        except ValueError as e:
            print("Introduce the date available in the format YYYY-MM-DD. \n", e)
    elif options == 7:
        print("Recommendations Market")
        return stock.recommendations.sort_values("Date", ascending=False).head(15)
    else:
        print("The introduced options are incorrect. Please, introduce options between 1 and 7.")    
