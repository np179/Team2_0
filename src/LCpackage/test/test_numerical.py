import pytest
import numpy as np
import numerical as nu

def test_rechne_autofct(test_wfauto):
    assert np.array_equal(nl.calc_auto(test_wfauto[0]), test_wfauto[1])
