import pytest
import numpy as np
import sort as st


@pytest.mark.parametrize('myval, result',
                         [
                             (np.array([4, 3, 2, 1]), all(np.array([1, 2, 3, 4]))),
                             (np.array([23, 52, 23, 52, 23, 52]),
                              all(np.array([23, 23, 23, 52, 52, 52]))),
                             (np.array([6, 422, 521123, 2223]),
                              all(np.array([6, 422, 2223, 521123])))
                         ])
def test_sort(myval, result):
    assert all(st.sort(myval)) == result
