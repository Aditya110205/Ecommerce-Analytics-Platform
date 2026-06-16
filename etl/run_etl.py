from etl.run_transformations import (
    run_transformations
)

from etl.load.load_warehouse import (
    load_table
)

from etl.extract.metadata import (
    update_last_processed_id
)


def run_etl():

    (
        dim_customer,
        dim_product,
        dim_date,
        fact_sales
    ) = run_transformations()

    load_table(
        dim_customer,
        "dim_customer"
    )

    load_table(
        dim_product,
        "dim_product"
    )

    load_table(
        dim_date,
        "dim_date"
    )

    load_table(
        fact_sales,
        "fact_sales"
    )

    if not fact_sales.empty:

        latest_order_id = (
            fact_sales["order_id"].max()
        )

        update_last_processed_id(
            int(latest_order_id)
        )

        print(
            f"Metadata updated to {latest_order_id}"
        )

    print(
        "Warehouse load completed"
    )


if __name__ == "__main__":

    run_etl()