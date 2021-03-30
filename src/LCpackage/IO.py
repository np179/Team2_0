import numpy as np
import matplotlib.pyplot as plt


def read_in_np(filedir, filename):
    ''' Reads in a .csv-type File to a Dataframe
Args:
filedir([String]): Directionary where the file is located
filename([String]): File which contains Dataframe

Returns:
Dataframe: Data from file as a numpy array
    '''
    name = '{}{}'.format(filedir, filename)
    print('Reading from file {} - numpy'.format(name))
    data = np.loadtxt(name, skiprows=1)
    data = data.T
    return data


def plot_and_save_function(time , data):
    '''Plots a given dataframes with time on the x-axis and data on \
    the y-axis and saves it
    Args:
        data: array with the same length as the time array
        time: array with same lenght as the data array
    '''
    plt.plot( time , data ) #plot freq gegn signal
    plt.savefig('Plot.pdf') #speichern
    
