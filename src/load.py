
import pandas as pd

DATA_FILE_NAME = "large_sales_data.csv"

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Data ingestion and cleaning.
    """
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    df = df.astype({'quantity': 'int64', 'price': 'float64'})
    df['total_sale'] = df['quantity'] * df['price']
    return df

