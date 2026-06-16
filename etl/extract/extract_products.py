import pandas as pd

from api.database.connection import engine


def extract_products():

    query = """
    SELECT *
    FROM products
    """

    return pd.read_sql(
        query,
        engine
    )


if __name__ == "__main__":

    df = extract_products()

    print(df.head())