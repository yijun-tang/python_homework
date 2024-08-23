import os
import unittest as ut

from src.load import load_and_clean_data
from src.visualization import generate_sales_charts

TEST_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

class TestVirtualization(ut.TestCase):
    def test_basic(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "large_sales_data.csv")
        df = load_and_clean_data(file_path)
        generate_sales_charts(df)

if __name__ == "__main__":
    ut.main()
