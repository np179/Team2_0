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


def check_significant_np(data, thresh):
    '''Checks if a coloum a given array is below a given threshhold and gives out a '''
    indices = np.nonzero(np.var(data, axis=1) > thresh)
    data_out = data[indices]
    return data_out, indices


def do_dft_real(data, tmax):
    '''Calculates the direct fouriertransformation of a given data and
    the frequencies of a given time
    Args:

    data: a real-valued numpy array
    tmax: a numpy array which discribes the time, has to have same length as data file

    Returns:
    an array with direct fourier transformed data and
    an array containing the sample frequencies

    '''
    signal = np.fft.rfft(data)
    signal = signal.real
    freq = np.fft.rfftfreq(tmax)
    return(signal, freq)


def plot_and_save_function(time, data):
    '''Plots a given dataframes with time on the x-axis and data on the y-axis and saves it
    data: array with the same length as the time array
    time: array with same lenght as the data array
    '''
    # plot freq gegn signal
    plt.plot(time, data)
    # speichern
    plt.savefig('Plot.pdf')


def drop_column(data, n):
    '''Selects a certain column of an array and stores the column in a vector
    data: array with data
    n: number of the column which should be stored in a vector
    '''
    df = data[n]
    print(df)


def make_complex(data):
    real = data[0::2]
    imag = data[1::2]
    # zusammensetzen der beiden Teile
    comp_fct = real + 1j * imag
    print(comp_fct)


def rechne_autofct(data):
    '''calculates the '''
    # leere (null) matrix mit laenge von komplexer
    autofct = np.zeros(len(data[0]), dtype=complex)
    for i in range(0, len(data[0])):
        # funktion von oben
        autofct[i] = np.sum(data[:, 0] * np.conjugate(data[:, i]))
    return autofct


def do_dft(data, time):
    data_dft = np.fft.fft(data)
    time_dft = np.fft.fftfreq(len(time))
    return(data_dft, time_dft)
