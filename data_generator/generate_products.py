import pandas as pd
import random


CATEGORIES = [
    "Electronics",
    "Books",
    "Fashion",
    "Home",
    "Sports"
]


def generate_products(num_products=50):

    products = []

    for product_id in range(1, num_products + 1):

        products.append(
            {
                "product_id": product_id,
                "product_name": f"Product_{product_id}",
                "category": random.choice(CATEGORIES),
                "price": round(
                    random.uniform(10, 1000),
                    2
                )
            }
        )

    return pd.DataFrame(products)


if __name__ == "__main__":

    df = generate_products()

    print(df.head())