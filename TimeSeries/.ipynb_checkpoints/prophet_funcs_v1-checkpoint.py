"""" This file contains functions used in of preprocess downloaded crypto close data """


#python packages

from datetime import datetime
import pandas as pd
import yfinance as yf
import pandas as pd


'''Function:datecheck 
this function is used to check to make sure that the last date is not tomorrows date. 
Yahoo Finance may pull data from a timezone that is in the future for some crypto close data.'''
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



