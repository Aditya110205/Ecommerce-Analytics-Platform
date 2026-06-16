import pandas as pd
import random

from datetime import datetime, timedelta


def generate_orders(
    num_orders=1000,
    max_customer_id=100,
    max_product_id=50
):

    orders = []

    for order_id in range(1, num_orders + 1):

        quantity = random.randint(1, 5)

        price = round(
            random.uniform(10, 1000),
            2
        )

        amount = round(
            quantity * price,
            2
        )

        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.randint(
                    1,
                    max_customer_id
                ),
                "product_id": random.randint(
                    1,
                    max_product_id
                ),
                "quantity": quantity,
                "amount": amount,
                "created_at":
                    datetime.now()
                    - timedelta(
                        days=random.randint(0, 30)
                    )
            }
        )

    return pd.DataFrame(orders)


if __name__ == "__main__":

    df = generate_orders()

    print(df.head())