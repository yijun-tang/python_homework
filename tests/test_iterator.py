import unittest as ut
from src.iterator import DateRangeIterator
from datetime import datetime


class TestIterator(ut.TestCase):
    def test_invalid_date_type(self):
        with self.assertRaises(TypeError):
            DateRangeIterator(datetime(2024, 8, 1), "2024-08-05")

    def test_empty_date_iterator(self):
        date_iter = DateRangeIterator(datetime(2024, 8, 6), datetime(2024, 8, 5))

        with self.assertRaises(StopIteration) as _:
            next(date_iter)

    def test_normal_date_iterator(self):
        date_iter = DateRangeIterator(datetime(2024, 8, 1), datetime(2024, 8, 5))

        self.assertEqual(next(date_iter).strftime("%Y-%m-%d"), "2024-08-01")
        self.assertEqual(next(date_iter).strftime("%Y-%m-%d"), "2024-08-02")
        self.assertEqual(next(date_iter).strftime("%Y-%m-%d"), "2024-08-03")
        self.assertEqual(next(date_iter).strftime("%Y-%m-%d"), "2024-08-04")
        self.assertEqual(next(date_iter).strftime("%Y-%m-%d"), "2024-08-05")
        with self.assertRaises(StopIteration) as _:
            next(date_iter)


if __name__ == "__main__":
    ut.main()
