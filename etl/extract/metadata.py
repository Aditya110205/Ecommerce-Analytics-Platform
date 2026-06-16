import pandas as pd

from sqlalchemy import text

from api.database.connection import engine


def get_last_processed_id():

    query = """
    SELECT last_processed_id
    FROM etl_metadata
    WHERE pipeline_name='orders'
    """

    df = pd.read_sql(query, engine)

    if df.empty:
        return 0

    return int(df.iloc[0]["last_processed_id"])


def update_last_processed_id(last_id):

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                UPDATE etl_metadata
                SET last_processed_id = :last_id
                WHERE pipeline_name='orders'
                """
            ),
            {"last_id": last_id}
        )