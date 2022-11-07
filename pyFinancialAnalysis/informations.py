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

# e.g. get_specific_information("AAPL", 1, "2022-10-10")

def get_company_stock_information(ticker_name, start_time, end_time, period_stock):
    try:
        dataframe = pd.DataFrame()
        stocks = ticker_name
        for stock in stocks:
            dataframe[stock] = yf.Ticker(stock).history(start_time = start_time, end_time = end_time)[period_stock]
        return dataframe
    except ValueError as e:
        print("Introduce the correct format of date. YYYY-MM-DD. \n", e)
# e.g. get_company_stock_information(["AAPL", "AMZN"], "2022-10-01", "2022-10-20", "Close")

def find_index_date(dataframe, date):
    try: 
        dataframe_reset = dataframe.reset_index()
        dataframe_new = []
        for row in dataframe_reset["Date"]:
            information_row = str(row)[0:10]
            dataframe_new.append(information_row)
        dataframe_concat = pd.DataFrame(dataframe_new).rename(columns = {0:"Dates"})
        dataframe_result = pd.concat([dataframe.reset_index(), dataframe_concat], axis = 1)
        dataframe_result = dataframe_result.drop(["Date"], axis = 1)
        indexs = dataframe_result.index[dataframe_result["Dates"]==date].tolist()
        return indexs[0]
        # print(f'The index of date {date} is {indexs[0]}.')
    except ValueError as e:
        print("Introduce the correct format of date in the function. YYYY-MM-DD. \n", e)

# e.g. found_index_date(dataframe, "2022-10-20")
"""
    First, you need to create a dataframe using the function: get_company_stock_information().
    Next, you need to store that dataframe in a variable. e.g. dataframe = get_company_stock_information().
    Then, you must introduce the variable in the function with the other parameter: find_index_date().
    Finally, you will get the index of the date you were looking for.
"""
    