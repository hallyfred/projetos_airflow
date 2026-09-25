import datetime

from airflow import DAG
from airflow.operators.python import EmptyOperator

minha_dag = DAG(
    dag_id="exemplo_dag_3",
    start_date=datetime.datetime(2025, 4, 24),
    description="A simple DAG with four tasks",
    schedule="daily",
    catchup=False
)

EmptyOperator1 = EmptyOperator(
    task_id="EmptyOperator1",
    dag=minha_dag
)