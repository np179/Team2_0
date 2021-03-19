import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

def read_in_df(filedir, filename):
    """[Read a .csv-type File to a DataFrame]

    Args:
        filedir ([String]): [Name of directory in which data is located] \n
        filename ([String]): [Name of file which contains data]

    Returns:
        [DataFrame]: [DataFrame with data from .csv indicated through input ]
    """
    name = '{}{}'.format(filedir, filename)     #creates filedir-filename "merge"
    print('Reading from file {} - pandas'.format(name))    
    data = pd.read_csv(name, r'\s+')                       #turn csv into dataframe
    return data

def del_below(df,threshhold):
    """[A function which takes a dataframe and checks the variance of the columns against a given threshhold, deletes IN PLACE if variance falls below threshhold]

    Args:
        df ([DataFrame]): [DataFrame to be checked] \n
        threshhold ([Integer or Float]): [Sets threshhold to check variance against]

    Returns:
        [DataFrame]: [DataFrame without the columns with variance below threshhold]
    """
    dellist=[]                              #create a list which will hold the columns that have a variance below the threshhold
    for i in range(len(df.columns)):        #iterate over all columns
        if df.var()[i] < threshhold:        #identify the relevant columns to delete
            dellist.append(i)               #add their index to the list
    df.drop(df.columns[dellist], axis=1, inplace=True)      #delete the columns
    return df        