import os
import pandas as pd
import matplotlib.pyplot as plt

from src.analysis import SalesAnalyzer
from src.functional_analysis import map_monthly_sales

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def generate_sales_charts(data: pd.DataFrame) -> None:
    """
    Generates and saves sales charts based on the provided data.
    """
    charts_dir = os.path.join(PROJECT_DIR, "charts")
    # 1. Plot Monthly Sales Trend (Line Chart)
    monthly_sales = map_monthly_sales(data)
    months = pd.to_datetime(list(monthly_sales.keys()))
    sales = list(monthly_sales.values())
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales, marker="o", linestyle="-")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    # Annotate each point with its value
    for i, txt in enumerate(sales):
        plt.annotate(
            f"{txt:.2f}",
            (months[i], sales[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "monthly_sales_trend.png"))
    plt.close()

    sa = SalesAnalyzer(data)
    # 2. Show Top 5 Products by Sales (Bar Chart)
    top_products_list = sa.top_products(5)
    products = [item[0] for item in top_products_list]
    product_sales = [item[1] for item in top_products_list]
    plt.figure(figsize=(10, 6))
    bars = plt.bar(products, product_sales)
    plt.title("Top 5 Products by Sales")
    plt.xlabel("Product ID")
    plt.ylabel("Total Sales")
    # Annotate each bar with its value
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
        )
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "top_5_products_by_sales.png"))
    plt.close()

    # 3. Display Customer Spending Distribution (Histogram)
    spending_data = sa.customer_spending(-1)
    spending_amounts = [
        amount for _, amount in spending_data
    ]  # Extract spending amounts
    plt.figure(figsize=(10, 6))
    plt.hist(spending_amounts, bins=20)
    plt.title("Customer Spending Distribution")
    plt.xlabel("Spending Amount")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(charts_dir, "customer_spending_distribution.png"))
    plt.close()
