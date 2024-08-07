import pandas as pd
import numpy as np

def get_any_machine(machineID, df):
    '''
    given a machineID(int) 1 through 100 and a dataframe(df), this function returns a dataframe with only values that match the machine ID
    '''
    df = df.loc[df['machineID'] == machineID]
    df = df.drop(['Unnamed: 0'], axis = 1)
    return df

def convert_column_bool(df, column):
    '''
    given a dataframe(df) and a column(str) this function converts values in those columns into boolean objects
    '''
    df[column] = df[column].fillna(0).astype(bool)
    return df

def find_future_fails(df):
    '''
    given a dataframe(df) with columns 'future_fail'(bool), 'failure_ID'(bool), 'datetime'(datetime object) and 'machineID'(int)
    this function returns the dataframe with the values in 'future_fail' altered so that a value of True represents the machine experiencing a failure at that index or the next full day
    '''
    df['future_fail'] = (df[['failureID', 'machineID']]\
        .sort_index(ascending=False)    
        .groupby(['machineID'], as_index=False)
        .rolling(window=24)
        .sum()
        .sort_index())['failureID'].apply(lambda x: x if pd.isnull(x) else x > 0)
    return df

def cut_inconclusive_data(df, column):
    '''
    given a dataframe(df) and a column(str) this function removes all rows of the dataframe where the value in that column in NaN
    '''
    df.dropna(subset=[column], inplace=True)
    return df

def join_onehotencode()
    '''
    
    '''