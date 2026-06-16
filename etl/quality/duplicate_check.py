def run_duplicate_check(df):

    duplicates = df.duplicated().sum()

    if duplicates > 0:

        raise ValueError(
            f"{duplicates} duplicates found"
        )

    return True