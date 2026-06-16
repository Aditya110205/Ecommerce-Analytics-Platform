import pandas as pd

from api.database.connection import engine

from etl.extract.metadata import (
    get_last_processed_id
)


def extract_orders():

    last_id = get_last_processed_id()

    query = f"""
    SELECT *
    FROM orders
    WHERE order_id > {last_id}
    ORDER BY order_id
    """

    df = pd.read_sql(
        query,
        engine
    )

    return df


if __name__ == "__main__":

    orders = extract_orders()

    print(
        f"Extracted {len(orders)} rows"
    )

    print(
        orders.head()
    )