from time import sleep

def first_task():
    print("First task executed")
    sleep(2)  # Simulate a delay for the first task

def second_task():
    print("Second task executed")
    sleep(2)  # Simulate a delay for the second task


def third_task():
    print("Third task executed")
    sleep(2)  # Simulate a delay for the third task


def pipeline():
    first_task()
    second_task()
    third_task()
    print("Pipeline completed") 

if __name__ == "__main__":
    pipeline()    