import asyncio
import random
from typing import Dict
import numpy as np
from faker import Faker
from src.analysis import SalesAnalyzer


async def simulate_sales_stream(channel: asyncio.Queue, num_updates: int) -> None:
    """
    Simulate a stream of sales updates.
    """
    for i in range(num_updates):
        # Simulate a delay with a random interval
        await asyncio.sleep(random.uniform(0.5, 2.0))

        # Generate a random sales update
        received_data = generate_random_sale_data()

        await channel.put(received_data)
        print(f"Sent {i}th sale data...")


async def process_sales_updates(
    channel: asyncio.Queue, analyzer: SalesAnalyzer, num_updates: int
) -> None:
    """
    Process sales updates received from the simulate_sales_stream coroutine.
    """
    updates_processed = 0
    while updates_processed < num_updates:
        sale_data = await channel.get()  # Block until item is available
        analyzer.append_sale_data(sale_data)
        updates_processed += 1
        channel.task_done()  # Signal that the item has been processed
        print(f"Appended one new row...")


def generate_random_sale_data() -> Dict:
    """
    Generate a single row of random sales data.
    """
    fake = Faker()
    return {
        "date": fake.date_this_year(),
        "product_id": f"P{np.random.randint(100, 999)}",
        "quantity": np.random.randint(1, 20),
        "price": round(np.random.uniform(5.0, 500.0), 2),
        "customer_id": f"C{np.random.randint(100, 999)}",
    }
