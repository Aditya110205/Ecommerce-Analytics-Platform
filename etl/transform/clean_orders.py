def clean_orders(df):

    df = df.drop_duplicates()

    df = df.dropna()

    return df