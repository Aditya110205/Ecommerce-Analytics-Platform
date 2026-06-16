def run_null_check(df):

    if df.isnull().sum().sum() > 0:

        raise ValueError(
            "Null values detected"
        )

    return True