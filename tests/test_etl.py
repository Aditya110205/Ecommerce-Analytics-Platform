import pandas as pd

from etl.run_quality_checks import (
    run_all_checks
)


def test_quality_pipeline():

    df = pd.DataFrame(
        {
            "quantity": [1, 2],
            "amount": [100, 200]
        }
    )

    assert run_all_checks(df)