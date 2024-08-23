import os
import unittest as ut
import pandas as pd
from src.functional_analysis import filter_high_value_sales, map_monthly_sales, reduce_to_total_revenue
from src.load import load_and_clean_data

TEST_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

class TestFunctionalAnalyzer(ut.TestCase):
    def test_filter_high_value_sales_invalid_input(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = pd.read_csv(file_path)

        with self.assertRaises(ValueError):
            filter_high_value_sales(df, 100.0)

    def test_filter_high_value_sales_normal(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = load_and_clean_data(file_path)

        filtered = filter_high_value_sales(df, 300.0)

        self.assertEqual(len(filtered), 2)

    def test_map_monthly_sales_invalid_input(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "functional.csv")
        df = pd.read_csv(file_path)

        with self.assertRaises(ValueError):
            map_monthly_sales(df)

    def test_map_monthly_sales_normal(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = load_and_clean_data(file_path)
        expected_output = {
            '2023-02': 225.48,
            '2023-04': 523.18,
            '2023-07': 141.63,
            '2023-10': 223,
            '2023-11': 333.84,
            '2023-12': 465.14
        }

        mapped = map_monthly_sales(df)

        for e1, e2 in zip(mapped.items(), expected_output.items()):
            month1, total1 = e1
            month2, total2 = e2
            self.assertEqual(month1, month2)
            self.assertAlmostEqual(total1, total2, delta=1e-9)

    def test_reduce_to_total_revenue_invalid_input(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = pd.read_csv(file_path)

        with self.assertRaises(ValueError):
            reduce_to_total_revenue(df)

    def test_reduce_to_total_revenue_normal(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = load_and_clean_data(file_path)

        total_revenue = reduce_to_total_revenue(df)

        self.assertAlmostEqual(total_revenue, 1912.27, delta=1e-9)


if __name__ == '__main__':
    ut.main()
