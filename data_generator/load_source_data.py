from api.database.connection import engine

from data_generator.generate_customers import (
    generate_customers
)

from data_generator.generate_products import (
    generate_products
)

from data_generator.generate_orders import (
    generate_orders
)


def load_customers():

    customers_df = generate_customers(100)

    customers_df.to_sql(
        "customers",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {len(customers_df)} customers"
    )


def load_products():

    products_df = generate_products(50)

    products_df.to_sql(
        "products",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {len(products_df)} products"
    )


def load_orders():

    orders_df = generate_orders(
        num_orders=1000,
        max_customer_id=100,
        max_product_id=50
    )

    orders_df.to_sql(
        "orders",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {len(orders_df)} orders"
    )


if __name__ == "__main__":

    load_customers()

    load_products()

    load_orders()

    print(
        "Source data load complete"
    )