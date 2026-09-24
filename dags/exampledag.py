from datetime import datetime
from time import sleep

from airflow.decorators import dag, task

@dag(
    dag_id="example_dag",    
    start_date=datetime(2025, 4, 24),
    description="A simple DAG with four tasks",
    schedule_interval="*****",
    catchup=False #backfill is disabled
)

def pipeline():
    @task
    def first_task():
        print("First task executed")
        sleep(2)  # Simulate a delay for the first task
    @task
    def second_task():
        print("Second task executed")
        sleep(2)  # Simulate a delay for the second task

    @task
    def third_task():
        print("Third task executed")
        sleep(2)  # Simulate a delay for the third task
    @task
    def forth_task():
        print("Forth task executed")
        sleep(2)  # Simulate a delay for the forth task    


    
    t1 = first_task()
    t2 = second_task()
    t3 = third_task()
    t4 = forth_task()

    t1 >> t2 >> t3 >> t4