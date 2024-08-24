import asyncio
import os
import unittest as ut

from src.analysis import SalesAnalyzer
from src.async_processing import process_sales_updates, simulate_sales_stream
from src.load import load_and_clean_data

TEST_DATA_DIR = os.path.dirname(os.path.abspath(__file__))


class TestAsyncProcessing(ut.IsolatedAsyncioTestCase):
    async def test_producer_consumer(self):
        file_path = os.path.join(TEST_DATA_DIR, "data", "empty.csv")
        df = load_and_clean_data(file_path)
        sa = SalesAnalyzer(df)
        channel = asyncio.Queue(10)

        await asyncio.gather(
            simulate_sales_stream(channel, 5), process_sales_updates(channel, sa, 3)
        )

        # print(sa.cleaned_df)

        self.assertEqual(len(sa.cleaned_df), 3)


if __name__ == "__main__":
    ut.main()
