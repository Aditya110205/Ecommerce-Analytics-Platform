import pandas as pd

from etl.transform.build_fact_sales import build_fact_sales

df = pd.DataFrame({
    "order_id":[1],
    "customer_id":[10],
    "product_id":[20],
    "quantity":[2],
    "amount":[100],
    "created_at":["2026-01-01"]
})

fact = build_fact_sales(df)

print(fact.columns)