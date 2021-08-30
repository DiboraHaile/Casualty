import unittest
import os
import sys
import numpy as np
sys.path.append(os.path.abspath(os.path.join('./')))

from scripts.loading_data import *
from scripts.feature_engineering import FeatureEngineering

# load data
df = load_csv("data/data.csv")
df = df.drop(columns=["Unnamed: 32"])
class TestDataLoader(unittest.TestCase):
    """
		A class for unit-testing function in the feature_engineering.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.fe = FeatureEngineering(df)

    def test_prepare_X_y(self):
        self.fe.prepare_X_y()  
        self.assertIsNotNone(self.fe.X)
        self.assertIsNotNone(self.fe.y)
        self.assertEqual(type(self.fe.X), np.ndarray)
        self.assertEqual(type(self.fe.y), np.ndarray)

    def test_prepare_split_X_y(self):
        self.fe.prepare_data()  
        self.assertIsNotNone(self.fe.X_train)
        self.assertIsNotNone(self.fe.y_train)
        self.assertIsNotNone(self.fe.X_test)
        self.assertIsNotNone(self.fe.y_test)
        # self.assertItemsEqual(np.concat(self.fe.X_train,self.fe.X_test),self.fe.X)
    
    def test_return_X_y(self):
        self.fe.prepare_data()
        self.assertEqual(self.fe.return_X_y(),(self.fe.X,self.fe.y))
    
    def test_return_split_X_y(self):
        self.fe.prepare_data()
        self.assertEqual(self.fe.return_split_X_y(),(self.fe.X_train,self.fe.X_test,self.fe.y_train,self.fe.y_test))

    def test_select_features(self):
        self.fe.execute_feature_engineering()
        check = all(item in self.fe.df for item in self.fe.selected_features)
        self.assertEqual(check,True)

if __name__ == '__main__':
	unittest.main()
