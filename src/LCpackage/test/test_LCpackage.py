import pytest
import numpy as np
import pandas as pd
import statistical as st 


@pytest.mark.parametrize('df_in, df_out',
                            [
                                (pd.DataFrame( data = {'col1':[1,1,1,1], 'col2':[1,2,3,4]}), pd.DataFrame( data = {'col2':[1,2,3,4]}))
                            ])

def test_del_below(df_in, df_out):
    assert all(st.del_below(df_in, 10E-5)) == all(df_out)