import os
import unittest as ut
from unittest.mock import patch
from src.load import load_and_clean_data
from src.analysis import SalesAnalyzer

TEST_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

class TestPerfMonitor(ut.TestCase):
    def setUp(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "top_products.csv")
        df = load_and_clean_data(file_path)
        self.analyzer = SalesAnalyzer(df)
    
    @patch('logging.Logger.info')
    def test_top_products_logging(self, mock_info):
        self.analyzer.top_products(3)

        log_messages = [call[0][0] for call in mock_info.call_args_list]
        self.assertAnyLogContains(log_messages, "Function 'top_products' called with arguments")
        self.assertAnyLogContains(log_messages, "Function 'top_products' executed")

    @patch('logging.Logger.info')
    def test_daily_sales_logging(self, mock_info):
        self.analyzer.daily_sales()

        log_messages = [call[0][0] for call in mock_info.call_args_list]
        self.assertAnyLogContains(log_messages, "Function 'daily_sales' called with arguments")
        self.assertAnyLogContains(log_messages, "Function 'daily_sales' executed")

    @patch('logging.Logger.info')
    def test_customer_spending_logging(self, mock_info):
        self.analyzer.customer_spending(3)

        log_messages = [call[0][0] for call in mock_info.call_args_list]
        self.assertAnyLogContains(log_messages, "Function 'customer_spending' called with arguments")
        self.assertAnyLogContains(log_messages, "Function 'customer_spending' executed")
    
    def assertAnyLogContains(self, log_messages, expected_text):
        """
        Assert that any of the log messages contain the expected text.
        """
        self.assertTrue(any(expected_text in message for message in log_messages),
                        f"No log message contains: {expected_text}")

if __name__ == "__main__":
    ut.main()
