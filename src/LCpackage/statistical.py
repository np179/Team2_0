import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

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

def plot_and_save_multiple(df, xaxis, var_name, value_name, path):
    """[Plot multiple columns of a DataFrame as lines against one specified column and save the plot in a designated location]

     Args:
        df ([DataFrame]): [Input DataFrame] \n
        xaxis ([String or Index]): [Designates Column of variable to plot against] \n
        var_name ([String]): [Describes the Columns plotted] \n
        value_name ([String]): [Description of the y-axis] \n
        path ([String]): [Designates location to save plot to]
    """
    df_2_melted=df_2.melt(xaxis, var_name=var_name, value_name=value_name)
    sn.relplot(data=df_2_melted, kind='line', x=xaxis, y=value_name, hue=var_name)  #write routine to check if file exists later
    plt.show()
    if Path(path).exists() == False:   
        plt.savefig(path)
    elif Path(path).exists() == True:
        print('{} already exists. Overwrite? Y/N'.format(path))
        check = input()
        if check == 'Y':
            plt.savefig(path)
            print('File {} was overwriten'.format(path))
        else:
            print('File {} was not overwriten'.format(path))
    
    if Path(path)
    plt.savefig(path)

def plot_and_save_single(df, xaxis, yaxis, path):    
    """[Plot a single column of a DataFrame as lines against one specified column and save the plot in a designated location]

    Args:
        df ([DataFrame]): [Input DataFrame] \n
        xaxis ([String or Index]): [Designates column to plot against] \n
        yaxis ([String or Index]): [Designates column to plot] \n
        path ([String]): [Designates location to save plot to] \n
    """
    sn.relplot(data=df, kind='line', x=xaxis, y=yaxis)   
    plt.savefig(path)
    plt.show()
    if Path(path).exists() == False:   
        plt.savefig(path)
    elif Path(path).exists() == True:
        print('{} already exists. Overwrite? Y/N'.format(path))
        check = input()
        if check == 'Y':
            plt.savefig(path)
            print('File {} was overwriten'.format(path))
        else:
            print('File {} was not overwriten'.format(path))