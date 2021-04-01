import pytest
import numpy as np
import pandas as pd
import statistical as st


@pytest.mark.parametrize('df_in, thresh, df_out',
                         [
                             (pd.DataFrame(data={'col1': [1, 1, 1, 1], 'col2': [1, 2, 3, 4]}),
                              10E-5, pd.DataFrame(data={'col2': [1, 2, 3, 4]})),
                             (pd.DataFrame(data={'col1': [1, 2, 10, 100], 'col2': [1, 2, 3, 4]}),
                              2, pd.DataFrame(data={'col1': [1, 2, 10, 100]}))
                         ])
def test_del_below(df_in, thresh, df_out):
    assert all(st.del_below(df_in, thresh)) == all(df_out)


@pytest.mark.parametrize('df_in_1, corr_matrix',
                         [
                             (pd.DataFrame(np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
                              columns=['col1', 'col2', 'col3']),
                              pd.DataFrame(np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
                              columns=['col1', 'col2', 'col3'], index=['col1', 'col2', 'col3'])),
                             (pd.DataFrame(np.array([[1, 2, 3],
                              [234, 123, 252], [2131, 2521, 5232]]),
                              columns=['col1', 'col2', 'col3']),
                              pd.DataFrame(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
                              columns=['col1', 'col2', 'col3'], index=['col1', 'col2', 'col3']))
                         ])
def test_correlation(df_in_1, corr_matrix):
    assert all(st.correlation(df_in_1)) == all(corr_matrix)


@pytest.mark.parametrize('corr_in, corr_out',
                         [
                             (pd.DataFrame(np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
                              columns=['col1', 'col2', 'col3'], index=['col1', 'col2', 'col3']),
                              pd.DataFrame(np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]]),
                              columns=['col1', 'col2', 'col3'], index=['col1', 'col2', 'col3'])),
                             (pd.DataFrame(np.array([[1, 2], [3, 4]])),
                              pd.DataFrame(np.array([[0, 2], [0, 0]])))
                         ])
def test_reduced(corr_in, corr_out):
    assert all(st.reduced(corr_in)) == all(corr_out)


@pytest.mark.parametrize('corr_in_ , exclude, value',
                         [
                             (pd.DataFrame(np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]]),
                              columns=['col1', 'col2', 'col3'], index=['col1', 'col2', 'col3']),
                              False,
                              np.array([['col1', 'col2', 1], ['col1', 'col3', 1],
                                        ['col2', 'col3', 1]])),
                             (pd.DataFrame(np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]]),
                              columns=['col1', 'col2', 'col3'], index=['col1', 'col2', 'col3']),
                              'col2',
                              np.array([['col1', 'col3', 1]]))
                         ])
def test_get_values(corr_in_, exclude, value):
    assert np.array_equal(st.get_values(corr_in_, exclude), value)


@pytest.mark.parametrize('array_in, sorted',
                         [
                             (np.array([['a', 'b', 1], ['a', 'c', -100], ['a', 'd', -20]]),
                              np.array([['a', 'b', 1], ['a', 'd', -20], ['a', 'c', -100]])),
                             (np.array([[1, 3, 45], [1, 5, 32], [12, 43, 2], [1, 2, -90]]),
                              np.array([[12, 43, 2], [1, 5, 32], [1, 3, 45], [1, 2, -90]]))
                         ])
def test_sort_values(array_in, sorted):
    assert np.array_equal(st.sort_values(array_in), sorted)
