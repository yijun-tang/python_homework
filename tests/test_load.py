import os
import unittest as ut
import pandas as pd
from src.load import load_and_clean_data

TEST_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

class TestLoadAndCleanData(ut.TestCase):
    def test_empty(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "empty.csv")

        df = load_and_clean_data(file_path)

        self.assertTrue(df.empty)

    def test_missing_value(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "missing_value.csv")
        expected_output = pd.DataFrame({
            "date": ["2023-11-01", "2023-02-15"],
            "product_id": ["P005", "P029"],
            "quantity": [6, 4],
            "price": [13.28, 56.37],
            "customer_id": ["C991", "C378"]
        }).reset_index(drop=True)
        expected_output['date'] = pd.to_datetime(expected_output['date'])

        df = load_and_clean_data(file_path)
        df = df.reset_index(drop=True).drop(columns='total_sale')

        pd.testing.assert_frame_equal(df, expected_output)

    def test_checking_types(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "checking_types.csv")
        expected_types = pd.Series({
            'date': 'datetime64[ns]', 
            'product_id': 'object', 
            'quantity': 'int64', 
            'price': 'float64', 
            'customer_id': 'object', 
            'total_sale': 'float64'
        })

        df = load_and_clean_data(file_path)

        pd.testing.assert_series_equal(df.dtypes, expected_types)

    def test_new_column(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "new_column.csv")
        expected_total_sale = [79.68, 254.16, 225.48]

        df = load_and_clean_data(file_path)

        for e1, e2 in zip(df['total_sale'].tolist(), expected_total_sale):
            self.assertAlmostEqual(e1, e2, delta=1e-9)


if __name__ == '__main__':
    ut.main()
