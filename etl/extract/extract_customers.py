import pandas as pd

from api.database.connection import engine


def extract_customers():

    query = """
    SELECT *
    FROM customers
    """

    return pd.read_sql(
        query,
        engine
    )


if __name__ == "__main__":

    df = extract_customers()

    print(df.head())