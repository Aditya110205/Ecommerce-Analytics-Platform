import pandas as pd


def build_customer_dimension(customers_df):

    return customers_df[
        [
            "customer_id",
            "name",
            "email",
            "city"
        ]
    ].drop_duplicates()


def build_product_dimension(products_df):

    return products_df[
        [
            "product_id",
            "product_name",
            "category",
            "price"
        ]
    ].drop_duplicates()