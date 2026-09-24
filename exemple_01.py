from datetime import datetime
from time import sleep

from airflow.decorators import dag

@dag(
    dag_id="example_dag",
    start_date=datetime(2025, 4, 24),
    description="A simple DAG with four tasks",
    schedule="* * * * *",
    catchup=False #backfill is disabled
)

def pipeline():

    def first_task():
        print("First task executed")
        sleep(2)  # Simulate a delay for the first task

    def second_task():
        print("Second task executed")
        sleep(2)  # Simulate a delay for the second task


    def third_task():
        print("Third task executed")
        sleep(2)  # Simulate a delay for the third task

    def forth_task():
        print("Forth task executed")
        sleep(2)  # Simulate a delay for the forth task    


    def pipeline():
        first_task()
        second_task()
        third_task()
        forth_task()

pipeline()