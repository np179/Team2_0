import numpy as np
import pandas as pd


def del_below(df, threshhold):
    """[Takes a dataframe and checks the variance of the columns against a given threshhold,
        deletes in place if variance falls below threshhold.]

    Args:
        df ([DataFrame]): [DataFrame to be checked.]
        threshhold ([Integer or Float]): [Sets threshhold to check variance against.]

    Returns:
        [DataFrame]: [DataFrame without the columns with variance below threshhold.]
    """
    # create a list which will hold the columns that have a variance below the threshhold
    dellist = []
    for i in range(len(df.columns)):
        # iterate over all columns
        if df.var()[i] < threshhold:
            # identify the relevant columns to delete
            dellist.append(i)
            # add their index to the list
            # delete the columns
    df.drop(df.columns[dellist], axis=1, inplace=True)
    return df


def correlation(df):
    """[Get correlation matrix for a given Dataframe using Pearsons r.]

    Args:
        df ([Dataframe]): [DataFrame containing data to be correlated.]

    Returns:
        [DataFrame]: [DataFrame representing the correlation matrix.]
    """
    # get correlation matrix
    corr_matrix = df.corr(method='pearson')
    print(corr_matrix)
    return corr_matrix


def reduced(corr_matrix):
    """[Takes correlation matrix in form of DataFrame and sets lower triangular values
        and diagonal values to 0.]

    Args:
        corr_matrix ([DataFrame]): [Correlation matrix to be reduced.]

    Returns:
        [DataFrame]: [Reduced correlation matrix.]
    """
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


def get_values(df, exclude):
    """[Extract values from correlation matrix.]

    Args:
        df ([DataFrame]): [Correlation Matrix.]
        exclude ([String or Boolean]): [Designated parameter which is not of interest
         and can be dropped. Set to False to keep all.]

    Returns:
        [np.ndarray]: [np.ndarray containing the values and information
        about what was correlated.]
    """
    list_of_entries = []
    for i in range(len(df.index)):
        for k in range(len(df.columns)):
            if df.index[i] != exclude:
                if df.columns[k] != exclude:
                    if df.loc[df.index[i], df.columns[k]] != 0:
                        list_of_entries.append([df.index[i], df.columns[k], df.iloc[i, k]])
                        # list containing what was correlated and related values
    array = np.array(list_of_entries)
    return array


def sort_values(array_in):
    """[Takes a np.ndarray containing N rows and 3 columns, sorts
    the rows by absolute value of the entry in the third column.]

    Args:
        array_in ([np.ndarray]): [Array containing the values of a correlation matrix.]

    Returns:
        [np.ndarray]: [Sorted array containing values of a correlation matrix.]
    """
    # basic implementation of insertion sort slightly modified for the object
    for i in range(1, len(array_in)):
        key_item = array_in[i, 2]
        temp_0 = array_in[i, 0]
        temp_1 = array_in[i, 1]
        j = i-1
        while j >= 0 and abs(float(array_in[j, 2])) > abs(float(key_item)):
            array_in[j+1] = array_in[j]
            j = j-1
        array_in[j+1, 0] = temp_0
        array_in[j+1, 1] = temp_1
        array_in[j+1, 2] = key_item
    return array_in


def get_columns(df, x, y):
    """[Take two columns from a DataFrame and put them into a seperate DataFrame.]

    Args:
        df ([DataFrame]): [DataFrame containing the columns to be extracted.]
        x ([String]): [Designates 1st column to be extracted.]
        y ([String]): [Designated 2nd column to be extracted.]

    Returns:
        [DataFrame]: [DataFrame only constisting of the two designated columns.]
    """
    # extract the interesting columns ("vectors") into separate dataframes
    df_out = pd.DataFrame(index=df.index, columns=[x, y])
    df_out[x] = df[x]
    df_out[y] = df[y]
    return df_out


def get_distance(vectors):
    """[Calculate the euclidian distance between two vectors, represented as columns in a DataFrame.]

    Args:
        vectors ([DataFrame]): [DataFrame containing the two columns representing the vectors.]

    Returns:
        [Float]: [Euclidian distance of the vectors.]
    """
    # get distance between vectors by essentially creating a vector which points from one
    # to the other (difference of input vectors) and than calculating the length of the
    # new vector through (summ_components**2)**(1/2)
    diff_summ = 0
    for i in range(len(vectors.index)):
        diff_summ = diff_summ + (vectors.iloc[i, 0] - vectors.iloc[i, 1])**2
    distance = (diff_summ)**(1/2)
    return distance
