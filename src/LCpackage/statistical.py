import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from pathlib import Path

def read_in_df(filedir, filename):
    """[Read a .csv-type File to a DataFrame.]
    \n
    Args:
        filedir ([String]): [Name of directory in which data is located.] \n
        filename ([String]): [Name of file which contains data.]
    \n
    Returns:
        [DataFrame]: [DataFrame with data from .csv indicated through input.]
    """
    name = '{}{}'.format(filedir, filename)     #creates filedir-filename "merge"
    print('Reading from file {} - pandas'.format(name))    
    data = pd.read_csv(name, r'\s+')                       #turn csv into dataframe
    return data

def del_below(df,threshhold):
    """[Takes a dataframe and checks the variance of the columns against a given threshhold, deletes IN PLACE if variance falls below threshhold.]
    \n
    Args:
        df ([DataFrame]): [DataFrame to be checked.] \n
        threshhold ([Integer or Float]): [Sets threshhold to check variance against.]
    \n
    Returns:
        [DataFrame]: [DataFrame without the columns with variance below threshhold.]
    """
    dellist=[]                              #create a list which will hold the columns that have a variance below the threshhold
    for i in range(len(df.columns)):        #iterate over all columns
        if df.var()[i] < threshhold:        #identify the relevant columns to delete
            dellist.append(i)               #add their index to the list
    df.drop(df.columns[dellist], axis=1, inplace=True)      #delete the columns
    return df        

def plot_and_save_multiple(df, xaxis, var_name, value_name, path):
    """[Plot multiple columns of a DataFrame as lines against one specified column and save the plot in a designated location.]
    \n
     Args:
        df ([DataFrame]): [Input DataFrame.] \n
        xaxis ([String or Index]): [Designates Column of variable to plot against.] \n
        var_name ([String]): [Describes the Columns plotted.] \n
        value_name ([String]): [Description of the y-axis.] \n
        path ([String]): [Designates location to save plot to.]
    """
    df_2_melted=df_2.melt(xaxis, var_name=var_name, value_name=value_name)
    sn.relplot(data=df_2_melted, kind='line', x=xaxis, y=value_name, hue=var_name)  
    plt.show()
    if Path(path).exists() == False:   #check if file exists already, ask before overwrite
        plt.savefig(path)
    elif Path(path).exists() == True:
        print('{} already exists. Overwrite? Y/N'.format(path))
        check = input()
        if check == 'Y':
            plt.savefig(path)
            print('File {} was overwriten'.format(path))
        else:
            print('File {} was not overwriten'.format(path))

def plot_and_save_single(df, xaxis, yaxis, path):    
    """[Plot a single column of a DataFrame as lines against one specified column and save the plot in a designated location.]
    \n
    Args:
        df ([DataFrame]): [Input DataFrame.] \n
        xaxis ([String or Index]): [Designates column to plot against.] \n
        yaxis ([String or Index]): [Designates column to plot.] \n
        path ([String]): [Designates location to save plot to.] \n
    """
    sn.relplot(data=df, kind='line', x=xaxis, y=yaxis)   
    plt.savefig(path)
    plt.show()
    if Path(path).exists() == False:   #check if file exists already, ask before overwrite
        plt.savefig(path)
    elif Path(path).exists() == True:
        print('{} already exists. Overwrite? Y/N'.format(path))
        check = input()
        if check == 'Y':
            plt.savefig(path)
            print('File {} was overwriten'.format(path))
        else:
            print('File {} was not overwriten'.format(path))

def correlation(df,reduce):
    """[Get correlation matrix for a given Dataframe using Pearsons r.]
    \n
    Args:
        df ([Dataframe]): [DataFrame containing data to be correlated.] \n
        reduce ([Boolean]): [If True, lower triangular and diagonal values will be set to 0.] \n

    Returns:
        [DataFrame]: [DataFrame representing the correlation matrix.]
    """
    corr_matrix = df.corr(method='pearson')     #get correlation matrix
    print(corr_matrix)
    if reduce == True:
        df_temp = pd.DataFrame(index=corr_matrix.index, columns=corr_matrix.columns)      
        for i in range(len(corr_matrix.columns)):                               
            for k in range(len(corr_matrix.index)):                             
                if i == k:                                              
                    df_temp.iloc[i, k] = 0         
                elif i > k:
                    df_temp.iloc[i, k] = 0
                else:
                    df_temp.iloc[i, k] = 1
        corr_matrix_reduced = corr_matrix*df_temp
        print(corr_matrix_reduced)
        return corr_matrix_reduced
    else:
        return corr_matrix 

def safe_values(df, exclude, sort, path):
    """[Extract values from correlation matrix, and save sorted or unsorted to .txt-file.]
    \n
    Args:
        df ([DataFrame]): [Correlation Matrix.]\n
        exclude ([String]): [Variable whos correlation is to be excluded.]\n
        sort ([Boolean]): [Set to true for values to be sorted along a certain axis.]\n
        path ([String]): [Designates location to save data to.]

    """
    list_of_entries = []                              
    for i in range(len(df.index)):
        for k in range(len(df.columns)):        
            if df.index[i] != exclude :           
                if df.columns[k] != exclude :    
                    if df.loc[df.index[i], df.columns[k]] != 0 :        
                        list_of_entries.append([df.index[i], df.columns[k], df.iloc[i, k]])
    list_of_entries = np.array(list_of_entries)     #list containing what was correlated and related values
    array_in = list_of_entries
    print(array_in)

    if sort == True:
        for i in range(1,len(array_in)):           
            key_item = float(array_in[i,2])
            temp_0 = array_in[i,0]
            temp_1 = array_in[i,1]
            j = i-1                            
            while j >= 0 and abs(float(array_in[j,2])) > abs(key_item): 
                array_in[j+1]=array_in[j]
                j = j-1 
            array_in[j+1,0] = temp_0
            array_in[j+1,1] = temp_1
            array_in[j+1,2] = key_item

        if Path(path).exists() == False:   #check if file exists already, ask before overwrite
            np.savetxt(path, array_in, fmt = '%s', header = 'Correlated : x -> y -> Pearson r(x,y) \n', delimiter = ' -> ', footer = '\nSorted using insertion sort based on absolute value \n')
        elif Path(path).exists() == True:
            print('{} already exists. Overwrite? Y/N'.format(path))
            check = input()
            if check == 'Y':
                np.savetxt(path, array_in, fmt = '%s', header = 'Correlated : x -> y -> Pearson r(x,y) \n', delimiter = ' -> ', footer = '\nSorted using insertion sort based on absolute value \n')
                print('File {} was overwriten'.format(path))
            else:
                print('File {} was not overwriten'.format(path))

    else:
        if Path(path).exists() == False:   #check if file exists already, ask before overwrite
            np.savetxt(path, array_in, fmt = '%s', header = 'Correlated : x -> y -> Pearson r(x,y) \n', delimiter = ' -> ')
        elif Path(path).exists() == True:
            print('{} already exists. Overwrite? Y/N'.format(path))
            check = input()
            if check == 'Y':
                np.savetxt(path, array_in, fmt = '%s', header = 'Correlated : x -> y -> Pearson r(x,y) \n', delimiter = ' -> ')
                print('File {} was overwriten'.format(path))
            else:
                print('File {} was not overwriten'.format(path))