def run_revenue_check(df):

    calculated = (
        df["quantity"] *
        df["amount"]
    ).sum()

    if calculated <= 0:

        raise ValueError(
            "Revenue validation failed"
        )

    return True