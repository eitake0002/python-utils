import unittest
import random_data as rd
import pandas as pd
import numpy as np
import datetime

class TestRandomData(unittest.TestCase):

    def test_simple_df(self):
        data = rd.rand_int(10, 10)
        self.assertEqual(isinstance(data, np.ndarray), True)

    def test_random_str(self):
        data = rd.random_str(10)
        self.assertEqual(isinstance(data, str), True)

    def test_random_list_str(self):
        data = rd.random_list_str(10)
        self.assertEqual(isinstance(data, list), True)

    def test_random_df_str(self):
        data = rd.random_df_str(10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

    def test_random_datetime(self):
        data = rd.random_datetime()
        self.assertEqual(isinstance(data, datetime.datetime), True)

    def test_random_datetime(self):
        data = rd.random_datetime_list(10)
        self.assertEqual(isinstance(data, list), True)

    def test_random_datetime_df(self):
        data = rd.random_datetime_df(10)
        self.assertEqual(isinstance(data, pd.DataFrame), True)

if __name__ == '__main__':
    unittest.main()
