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

def plot_and_save_function(time , data):
    '''Plots a given dataframes with time on the x-axis and data on \
    the y-axis and saves it
    Args:
        data: array with the same length as the time array
        time: array with same lenght as the data array
    '''
    plt.plot( time , data ) #plot freq gegn signal
    plt.savefig('Plot.pdf') #speichern


def rechne_autofct(data):
    '''Function to compute the autocorrelation function from the
    given vectors

    Args:
        data (numpy array, complex): The wave function\
        over time.


    Returns:
        numpy array, complex: The autocorrelation function over time.
     '''
     time = data[0]
     data = np.delete(data, [0], axis=0)
     real = fct[0::2]
     imag = fct[1::2]
     wavefct = real + 1j*imag #zusammensetzen der beiden Teile
     aucofu = calc_auto(wavefc)
     return time, aucofu


 def help_autofct(data):
     '''Helps the rechne_autofct '''
     autofct = np.zeros(len(data[0]), dtype = complex) #leere (null) matrix mit laenge von komplexer
     for i in range(0,len(data[0])):
        autofct[i] = np.sum(data[:,0]*np.conjugate(data[:,i])) #funktion von oben
        return autofct

def do_real_dft(data):
    '''Calculates the real direct fourier transformation of a given data and
    the frequencies of a given time

    Args:

        data:  The data with time data in the\
        first row and the real-valued vectors in the following rows.

    Returns:
        numpy array, real; with the energy grid points of the direct fourier \
        and the fourier transformed function.

    '''
    tmax = len(wavef[0])
    signal = np.fft.rfft(efield_y)
    signal = signal.real
    freq = np.fft.rfftfreq(tmax)
    return(signal ,freq)

def do_complex_dft(data):
    '''Calculates the complex direct fouriertransformation of a given data and
    the frequencies of a given time

    Args:

        data:The data with time data in the\
        first row and the complex-valued vectors in the following rows.

    Returns:
        numpy array, complex; with the energy grid points of the direct fourier \
        and the fourier transformed function.

    '''
    tmax = len(wavef[0])
    data_dft = np.fft.fft(data)
    time_dft = np.fft.fftfreq(len(time))
    return(data_dft , time_dft )
