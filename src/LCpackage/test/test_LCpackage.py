import pytest
import numpy as np
import pandas as pd
import statistical as st 


@pytest.mark.parametrize('df_in, thresh, df_out',
                            [
                                (pd.DataFrame( data = {'col1':[1,1,1,1], 'col2':[1,2,3,4]}), 10E-5, pd.DataFrame( data = {'col2':[1,2,3,4]})),
                                (pd.DataFrame( data = {'col1':[1,2,10,100], 'col2':[1,2,3,4]}), 2, pd.DataFrame( data = {'col1':[1,2,10,100]}))
                            ])

def test_del_below(df_in, thresh, df_out):
    assert all(st.del_below(df_in, thresh)) == all(df_out)