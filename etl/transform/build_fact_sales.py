def build_fact_sales(orders_df):

    return orders_df[
        [
            "order_id",
            "customer_id",
            "product_id",
            "quantity",
            "amount",
            "created_at"
        ]
    ]