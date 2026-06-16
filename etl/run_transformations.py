from etl.extract.extract_customers import (
    extract_customers
)

from etl.extract.extract_products import (
    extract_products
)

from etl.extract.extract_orders import (
    extract_orders
)

from etl.transform.build_dimensions import (
    build_customer_dimension,
    build_product_dimension
)

from etl.transform.build_date_dimension import (
    build_date_dimension
)

from etl.transform.build_fact_sales import (
    build_fact_sales
)


def run_transformations():

    customers_df = extract_customers()

    products_df = extract_products()

    orders_df = extract_orders()

    dim_customer = build_customer_dimension(
        customers_df
    )

    dim_product = build_product_dimension(
        products_df
    )

    dim_date = build_date_dimension(
        orders_df
    )

    fact_sales = build_fact_sales(
        orders_df
    )

    print("dim_customer:", len(dim_customer))
    print("dim_product:", len(dim_product))
    print("dim_date:", len(dim_date))
    print("fact_sales:", len(fact_sales))

    return (
        dim_customer,
        dim_product,
        dim_date,
        fact_sales
    )


if __name__ == "__main__":

    run_transformations()