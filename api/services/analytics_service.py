import pandas as pd

from api.database.connection import engine


def get_daily_revenue():

    query = """
    SELECT
        DATE(created_at) AS sales_date,
        SUM(amount) AS total_revenue
    FROM fact_sales
    GROUP BY DATE(created_at)
    ORDER BY sales_date
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")


def get_top_products():

    query = """
    SELECT
        p.product_name,
        p.category,
        SUM(f.amount) AS total_revenue
    FROM fact_sales f
    JOIN dim_product p
      ON f.product_id = p.product_id
    GROUP BY
        p.product_name,
        p.category
    ORDER BY total_revenue DESC
    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")


def get_top_customers():

    query = """
    SELECT
        c.customer_id,
        c.name,
        SUM(f.amount) AS total_spent
    FROM fact_sales f
    JOIN dim_customer c
      ON f.customer_id = c.customer_id
    GROUP BY
        c.customer_id,
        c.name
    ORDER BY total_spent DESC
    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")


def get_monthly_sales():

    query = """
    SELECT
        YEAR(created_at) AS year,
        MONTH(created_at) AS month,
        SUM(amount) AS total_revenue
    FROM fact_sales
    GROUP BY
        YEAR(created_at),
        MONTH(created_at)
    ORDER BY
        year,
        month
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")