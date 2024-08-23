from typing import List, Tuple, Dict
import pandas as pd

class SalesAnalyzer:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with the cleaned DataFrame
        """
        self.cleaned_df = data

    def top_products(self, n: int) -> List[Tuple[str, float]]:
        """
        Return top N products by total revenue
        """
        grouped = self.cleaned_df.groupby('product_id')
        top_n = grouped['total_sale'].sum().nlargest(n)
        return list(zip(top_n.index, top_n.values))
    
    def daily_sales(self) -> Dict[str, float]:
        """
        Return a dictionary of total daily sales
        """
        grouped = self.cleaned_df.groupby('date')
        sum = grouped['total_sale'].sum()
        return sum.to_dict()
    
    def customer_spending(self, top: int) -> List[Tuple[str, float]]:
        """
        Return top customers by total spending
        """
        grouped = self.cleaned_df.groupby('customer_id')
        top_n = grouped['total_sale'].sum().nlargest(top)
        return list(zip(top_n.index, top_n.values))

