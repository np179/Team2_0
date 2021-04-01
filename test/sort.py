import numpy as np


def sort(array_in):
    if type(array_in) != np.ndarray:
        raise ValueError("Input must be np.ndarray.")
    for i in range(len(array_in)):
        key_item = array_in[i]
        j = i - 1
        while j > 0 and array_in[j] > key_item:
            array_in[j + 1] = array_in[j]
            j -= 1
    return array_in
