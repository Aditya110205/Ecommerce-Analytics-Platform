from api.database.connection import engine


def load_table(df, table_name):

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )