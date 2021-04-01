import numpy as np
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


def read_in_df(filedir, filename):
    """[Read a .csv-type File to a DataFrame.]

    Args:
        filedir ([String]): [Name of directory in which data is located.]
        filename ([String]): [Name of file which contains data.]

    Returns:
        [DataFrame]: [DataFrame with data from .csv indicated through input.]
    """
    # creates filedir-filename "merge"
    name = '{}{}'.format(filedir, filename)
    print('Reading from file {} - pandas'.format(name))
    if Path(name).exists is False:
        raise ValueError('Designated Path does not exist.')
    else:
        # turn csv into dataframe
        data = pd.read_csv(name, r'\s+')
    return data


def plot_single(df, xaxis, yaxis):
    """[Plot a single column of a DataFrame as lines against one specified column.]

    Args:
        df ([DataFrame]): [Input DataFrame.]
        xaxis ([String or Index]): [Designates column to plot against.]
        yaxis ([String or Index]): [Designates column to plot.]
    """
    sn.relplot(data=df, kind='line', x=xaxis, y=yaxis)
    plt.show()


def plot_multiple(df, xaxis, var_name, value_name):
    """[Plot multiple columns of a DataFrame as lines against one specified column.]

     Args:
        df ([DataFrame]): [Input DataFrame.]
        xaxis ([String or Index]): [Designates Column of variable to plot against.]
        var_name ([String]): [Describes the Columns plotted.]
        value_name ([String]): [Description of the y-axis.]
    """
    df_2_melted = df.melt(xaxis, var_name=var_name, value_name=value_name)
    sn.relplot(data=df_2_melted, kind='line', x=xaxis, y=value_name, hue=var_name)
    plt.show()


def save_fig(path):
    """[Check if a path exists already and ask for input before overwriting to save Plot to location.]

    Args:
        path ([String]): [Path to be checked and written to.]
    """
    # check if file exists already, ask before overwrite
    if Path(path).exists() is False:
        plt.savefig(path)
    elif Path(path).exists() is True:
        print('{} already exists. Overwrite? Y/N'.format(path))
        check = input()
        if check == 'Y':
            plt.savefig(path)
            print('File {} was overwriten'.format(path))
        else:
            print('File {} was not overwriten'.format(path))


def save_array(array, path):
    """[Takes a np.ndarray and saves it as .txt at
        designated location. Checks if file is already existing.]

    Args:
        array ([np.ndarray]): [Array to be saved as file.]
        path ([type]): [description]
    """
    # check if file exists already, ask before overwrite
    if Path(path).exists() is False:
        np.savetxt(path, array, fmt='%s', delimiter=' , ')
    elif Path(path).exists() is True:
        print('{} already exists. Overwrite? Y/N'.format(path))
        check = input()
        if check == 'Y':
            np.savetxt(path, array, fmt='%s', delimiter=' , ')
            print('File {} was overwriten'.format(path))
        else:
            print('File {} was not overwriten'.format(path))
