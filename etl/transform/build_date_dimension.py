import pandas as pd


def build_date_dimension(df):

    date_dim = pd.DataFrame()

    date_dim["date_key"] = pd.to_datetime(
        df["created_at"]
    ).dt.date

    date_dim["year"] = pd.to_datetime(
        df["created_at"]
    ).dt.year

    date_dim["month"] = pd.to_datetime(
        df["created_at"]
    ).dt.month

    date_dim["day"] = pd.to_datetime(
        df["created_at"]
    ).dt.day

    return date_dim.drop_duplicates()