from etl.quality.null_check import (
    run_null_check
)

from etl.quality.duplicate_check import (
    run_duplicate_check
)

from etl.quality.revenue_check import (
    run_revenue_check
)


def run_all_checks(df):

    run_null_check(df)

    run_duplicate_check(df)

    run_revenue_check(df)

    print(
        "All quality checks passed"
    )

    return True