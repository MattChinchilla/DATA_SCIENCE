# function to remove last record if date is greater than sysdate

from datetime import datetime
import pandas as pd

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



#Function to preprocess market data and format to prophet specific format

def preprocess(file):
    #Convert download file to time series of date and close
    file_ts = file[['Date','Close']]

    #rename columns 'ds' = datestamp and Y = Y value for prophet
    file_ts = file_ts.rename(columns={"Date": "ds", "Close": "y"})

    #Drop Na values from file
    df = file_ts.dropna(axis=0)
    return(df)