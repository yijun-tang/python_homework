from datetime import datetime, timedelta


class DateRangeIterator:
    def __init__(self, start_date, end_date):
        """
        Initializes with start_date and end_date.
        """
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise TypeError("Both start_date and end_date must be datetime instances.")
        self.current_date = start_date
        self.end_date = end_date

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next date in the range.

        Raises StopIteration when the end of the range is reached.
        """
        if self.current_date > self.end_date:
            raise StopIteration
        current = self.current_date
        self.current_date += timedelta(days=1)
        return current
