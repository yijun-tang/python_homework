import os
import unittest as ut
from src.load import load_and_clean_data
from src.analysis import SalesAnalyzer

TEST_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

class TestSalesAnalyzer(ut.TestCase):
    def test_top_products_empty(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "empty.csv")
        empty_df = load_and_clean_data(file_path)
        empty_sa = SalesAnalyzer(empty_df)

        top_three = empty_sa.top_products(3)

        self.assertEqual(len(top_three), 0)

    def test_top_products(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = load_and_clean_data(file_path)
        sa = SalesAnalyzer(df)
        expected_output = [('P014', 375.30), ('P002', 373.59), ('P008', 254.16)]

        top_three = sa.top_products(3)

        for e1, e2 in zip(top_three, expected_output):
            product_id1, total_revenue1 = e1
            product_id2, total_revenue2 = e2
            self.assertEqual(product_id1, product_id2)
            self.assertAlmostEqual(total_revenue1, total_revenue2, delta=1e-9)

    def test_daily_sales_empty(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "empty.csv")
        empty_df = load_and_clean_data(file_path)
        empty_sa = SalesAnalyzer(empty_df)

        ds = empty_sa.daily_sales()

        self.assertEqual(len(ds), 0)

    def test_daily_sales(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "daily_sales.csv")
        df = load_and_clean_data(file_path)
        sa = SalesAnalyzer(df)
        expected_output = {
            '2023-02-15': 225.48, 
            '2023-04-19': 523.18, 
            '2023-07-10': 141.63, 
            '2023-10-25': 223.0,
            '2023-11-01': 333.84,
            '2023-12-12': 465.14,
        }

        ds = sa.daily_sales()

        for e1, e2 in zip(ds.items(), expected_output.items()):
            k1, v1 = e1
            k2, v2 = e2
            self.assertEqual(k1.strftime("%Y-%m-%d"), k2)
            self.assertAlmostEqual(v1, v2, delta=1e-9)

    def test_customer_spending_empty(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "empty.csv")
        empty_df = load_and_clean_data(file_path)
        empty_sa = SalesAnalyzer(empty_df)

        top_three = empty_sa.customer_spending(3)

        self.assertEqual(len(top_three), 0)

    def test_customer_spending(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = load_and_clean_data(file_path)
        sa = SalesAnalyzer(df)
        expected_output = [('C906', 375.30), ('C267', 373.59), ('C425', 254.16)]

        top_three = sa.customer_spending(3)

        for e1, e2 in zip(top_three, expected_output):
            product_id1, total_revenue1 = e1
            product_id2, total_revenue2 = e2
            self.assertEqual(product_id1, product_id2)
            self.assertAlmostEqual(total_revenue1, total_revenue2, delta=1e-9)


if __name__ == '__main__':
    ut.main()
