'''This file defines packages and functions used in crypto_forecast notebook updated to v2'''

#python packages
from datetime import datetime
import pandas as pd
import yfinance as yf
import pandas as pd


'''
Function: FetchData
This function takes the input vars and uses the yfinance package to download data from the yahoo finance website.
FetchData has one input variable vars which is actually two inputs tickerStrings and period packaged into vars.
vars: tickerStrings,period
tickerStrings - This is a list of tickers to fetch from yfinance ex: tickerStrings = ['AAPL', 'MSFT']
period -  Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
'''

def FetchData(vars):
    tickerStrings,period = vars
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period = period)
        data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)
        df = pd.concat(df_list) # combine all dataframes into a single dataframe
    return(df)





'''
Function:datecheck 
this function is used to check to make sure that the last date is not tomorrows date. 
Yahoo Finance may pull data from a timezone that is in the future for some crypto close data.
'''
def datecheck(df):
    #Get todays date and convert to datetime format ymd
    today = datetime.today()
    
    #Get last date of dataframe
    last_dt = pd.to_datetime(df['ds'].tail(1))

    #test if last date is greater or equal to current datetime
    test_dt = last_dt <= today

    #if statement to remove last record from df given the last date is greater than current date
    if test_dt.bool() == True:
        return(df)
    else:
        df.drop(df.tail(1).index, inplace=True)
        return(df)
