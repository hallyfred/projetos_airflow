# aqui criaremos um exemplo de dag com quatro tarefas,
# onde a primeira tarefa será executada primeiro seguida pela segunda e terceira tarefas
# e finalmente a quarta tarefa será executada por último.


from datetime import datetime
from time import sleep

from airflow.decorators import dag, task

@dag(
    dag_id="pipeline_two",    
    start_date=datetime(2025, 4, 24),
    description="A simple DAG with four tasks",
    schedule="* * * * *",
    catchup=False #backfill is disabled
)

def pipeline_two():
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

    # configurando dependencias entre as tarefas
    # t2 e t3 dependem de t1, e t4 depende de t3
    t1.set_downstream([t2,t3])
    t3.set_downstream([t4])

pipeline_two()