# tests/test_debt.py

import unittest
import os
import pandas as pd
from pythainance.debt.loader import setup_debt_data, fix_format_debt_data
from pythainance.debt.analysis import load_debt_data, compute_government_debt

# from pythainance.debt import load_debt_data, compute_government_debt, setup_debt_data, fix_format_debt_data
# from pythainance import analysis


class TestDebtData(unittest.TestCase):
    def setUp(self):
        # Ensure the debt.xlsx file exists; if not, set up the data
        if not os.path.exists("pythainance/dataset/debt.xlsx"):
            setup_debt_data()
            fix_format_debt_data()
        self.df = load_debt_data()

    def test_data_loaded(self):
        """
        Test that the data is loaded into a DataFrame with content.
        """
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertTrue(len(self.df) > 0, "The DataFrame should contain data.")

    def test_government_debt(self):
        """
        Test that the computed government debt is a pandas Series and does not contain NaN values.
        """
        gov_debt = compute_government_debt(self.df)
        self.assertIsInstance(gov_debt, pd.Series)
        self.assertFalse(gov_debt.isnull().any(), "Government debt should not contain NaN values.")

if __name__ == "__main__":
    unittest.main()
