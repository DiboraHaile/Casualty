import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join('./')))

from scripts.loading_data import *


path = "data/data.csv"
class TestDataLoader(unittest.TestCase):
    """
		A class for unit-testing function in the loading_data.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.path = path

    def test_load_csv(self):
        df = load_csv(self.path)  
        self.assertEqual(df.empty, False)
    

if __name__ == '__main__':
	unittest.main()
