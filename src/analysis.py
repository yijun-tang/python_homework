from typing import List, Tuple, Dict
import pandas as pd
from src.perf_monitor import performance_monitor

class SalesAnalyzer:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with the cleaned DataFrame
        """
        self.cleaned_df = data
    
    def append_sale_data(self, row: Dict) -> None:
        """
        Append a newly received sale data to the cleaned dataframe.
        """
        if 'date' not in row.keys():
            raise ValueError("The sale data must contain a 'date' column")
        if 'product_id' not in row.keys():
            raise ValueError("The sale data must contain a 'product_id' column")
        if 'quantity' not in row.keys():
            raise ValueError("The sale data must contain a 'quantity' column")
        if 'price' not in row.keys():
            raise ValueError("The sale data must contain a 'price' column")
        if 'customer_id' not in row.keys():
            raise ValueError("The sale data must contain a 'customer_id' column")
        self.cleaned_df = pd.concat([self.cleaned_df, pd.DataFrame([row])], ignore_index=True)

    @performance_monitor
    def top_products(self, n: int) -> List[Tuple[str, float]]:
        """
        Return top N products by total revenue
        """
        grouped = self.cleaned_df.groupby('product_id')
        top_n = grouped['total_sale'].sum().nlargest(n)
        return list(zip(top_n.index, top_n.values))
    
    @performance_monitor
    def daily_sales(self) -> Dict[str, float]:
        """
        Return a dictionary of total daily sales
        """
        grouped = self.cleaned_df.groupby('date')
        sum = grouped['total_sale'].sum()
        return sum.to_dict()
    
    @performance_monitor
    def customer_spending(self, top: int) -> List[Tuple[str, float]]:
        """
        Return top customers by total spending
        """
        grouped = self.cleaned_df.groupby('customer_id')
        if top == -1:
            top_n = grouped['total_sale'].sum()
        else:
            top_n = grouped['total_sale'].sum().nlargest(top)
        return list(zip(top_n.index, top_n.values))

