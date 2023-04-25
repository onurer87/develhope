from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.opertors.python_operator import BranchPytonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.opertors.postgres_opertaor import PostgresOperator
import os
from datetime import datetime,timedelta
import json
import pandas as pd
import numpy as np
import time
import requests


./data: /opt/airflow/data


dag_default_args={
    'start_date':datetime(2023, 4,22)
    'retries':1
    'rety_delay':timedelta(minutes=1)
    'project_id':1
}

def get_data():
    ticker='IBM'
    url=""+API_KEY
    r=requests.get(url)
    data=r.json()

def checkpoint(**kwargs):
    pass


with DAG("checkpoint_dag",schedule='@daily',catchup=False,default_args=dag_default_args) as day_paython:

    task_0=PythonOperator(task_id='checkpoint_test_task',python_callable=checkpoint,op_kwargs={'tickers':''})
    task_1 = BashOperator(task_id='checkpopint_bash_operator',bash_command="")
    ta