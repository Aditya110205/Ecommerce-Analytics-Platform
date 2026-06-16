import pandas as pd

from etl.quality.null_check import (
    run_null_check
)


def test_null_check():

    df = pd.DataFrame(
        {
            "id": [1, 2]
        }
    )

    assert run_null_check(df)