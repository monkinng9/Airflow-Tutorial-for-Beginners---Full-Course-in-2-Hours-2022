from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
  'owner': 'chayut',
  'retires': 5,
  'retry_delay': timedelta(minutes=2) 
}

with DAG(
  dag_id = 'out_first_dagV4',
  default_args=default_args,
  description = 'This is our first dag that we write',
  start_date = datetime(2022, 7, 29, 2),
  schedule_interval = '@daily'
) as dag:
  task1 = BashOperator(
    task_id = 'first_task',
    bash_command="echo Hello World!"
  )

  task2 = BashOperator(
    task_id='second_task',
    bash_command="echo Hello World2!"
  )

  task3 = BashOperator(
    task_id='third_task',
    bash_command="echo Hello World3!"
  )

  task1 >> task2
  task1 >> task3