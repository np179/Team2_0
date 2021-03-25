import unittest
import numpy as np
import sort as st 

class test_sort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(all(st.sort(np.array([5,9,23,7]))), all(np.array([5,7,9,23])))

    def test_value(self):
        self.assertRaises(ValueError, st.sort, [5,9,23,7])