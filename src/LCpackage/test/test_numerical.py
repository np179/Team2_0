import pytest
import numpy as np
import numerical as nu

class build_wavefct: #erstellt die arrays und vectoren für den test
    def __init__(self):
        pass

    def init_array(self, dim1, dim2, val):  # zwei dimensionen und einen Value
        array = np.ones((dim1, dim2), dtype=complex)
        return(array*val)

    def init_vector(self, dim1 , val):
        vector = np.ones(dim1 , dtype=complex)
        return(vector*val)

@pytest.fixture(scope='module')
def init_object():
    obj = build_wavefct()          #objekt aus wavefunktion machen
    return obj

@pytest.fixture
def test_wfauto(init_obj):
    wavefct = init_obj.init_array(3, 3, 1.0)    #macht wf
    auto = init_obj.init_vector(3, 3.0)         #macht atuofct aus array
    return wavefct, auto



def test_rechne_autofct(test_wfauto):
    assert np.array_equal(nu.calc_autofct(test_wfauto[0]), test_wfauto[1]) #testet Überlappung
