
from functools import reduce
from typing import Dict, List
import pandas as pd

def filter_high_value_sales(data: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Filter rows in the DataFrame where the sales_value column exceeds the specified threshold.
    """
    # Ensure 'total_sale' is a column in the DataFrame
    if 'total_sale' not in data.columns:
        raise ValueError("The DataFrame must contain a 'total_sale' column")
    
    # Convert DataFrame to a list of tuples where each tuple represents a row
    rows = data.itertuples(index=False, name=None)

    # Define a lambda function to check if the total_sale exceeds the threshold
    filter_func = lambda row: row[data.columns.get_loc('total_sale')] > threshold

    # Use filter to get rows that satisfy the condition
    filtered_rows = filter(filter_func, rows)

    return pd.DataFrame(filtered_rows, columns=data.columns)

def map_monthly_sales(data: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate the total sales for each month and return as a dictionary.
    """
    # Ensure 'date' is a column in the DataFrame
    if 'date' not in data.columns:
        raise ValueError("The DataFrame must contain a 'date' column")
    
    # Create a new column for month-year in 'YYYY-MM' format
    data['month_year'] = data['date'].map(lambda date: date.strftime('%Y-%m'))

    # Group by 'month_year' and sum 'sale_value'
    monthly_sales = data.groupby('month_year')['total_sale'].sum()

    return monthly_sales.to_dict()

def reduce_to_total_revenue(data: pd.DataFrame) -> float:
    """
    Calculate the total revenue from the 'total_sale' column in the DataFrame.
    """
    # Ensure 'total_sale' is a column in the DataFrame
    if 'total_sale' not in data.columns:
        raise ValueError("The DataFrame must contain a 'total_sale' column")
    
    # Convert 'total_sale' column to a list
    total_sales: List[float] = data['total_sale'].tolist()

    return reduce(lambda x, y: x + y, total_sales, 0.0)
