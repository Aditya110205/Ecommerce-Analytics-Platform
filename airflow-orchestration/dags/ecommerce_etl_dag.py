from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="ecommerce_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="""
        cd /opt/airflow/project &&
        python -m etl.run_etl
        """
    )

    run_etl