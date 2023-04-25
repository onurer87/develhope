from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import os
from datetime import datetime, timedelta
import json
import pandas as pd
import numpy as np


dag_default_args = {
    'start_date':datetime(2023,4,22)
    'retries':1
    'retry_delay':timedelta(minutes=1)
    'project_id':1
}
API_key="f679f0fb96a62d4e095329b6d7de7d07"

def get_data():
    url="http://api.openweathermap.org/data/2.5/forecast?id=524901&appid="+API_key
    r=requests(url)
    data=r.json()
    dict=json.load(data)
    path= "/opt/airflow/data/DATA_LAKE"
    df=pd.DataFrame(dict)
    df.to_csv(path)
    
    

def load_data():
    df=pd.read_csv("/opt/airflow/data/DATA_LAKE/clean_data.csv")
    print(df)


with DAG("1checkpoint",schedule_interval=None, default_args=dag_default_args) as python_dag:

    data_get=PythonOperator("getting_data",pyhon_callable=get_data)
    data_clean=PythonOperator("cleaning_data",python_callable=clean_data)
    data_load = PythonOperator("laod_data",pyhton_callable=load_data)


    data_get>>data_clean>>data_load
    