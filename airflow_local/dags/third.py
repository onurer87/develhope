import requests 
import time 
import json 
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.python import BranchPythonOperator 
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta 
import pandas as pd 
import numpy as np 
import os

#exercise: write a DAG which is able to request market data for a list of stocks.
API_key='AZQ6QOXNR3NDY4N2'
list_of_stocks=['IBM','AAMC','ABT','BDTX']
# this list should be an input of your function. The functions names are left to help you
# you DAG should only have one task
def get_data(**kwargs):
    ticker= kwargs['tickers']
    for tick in ticker:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+tick+'&interval=5min&apikey='+API_key
        r = requests.get(url)
        try:    
            path= "/opt/airflow/data/DATA_CENTER/DATA_LAKE/"
            data = r.json()
            with open(path+"stock_market_raw_data_"+tick+'_'+str(time.time()), "w") as outfile:
                json.dump(data,outfile)
        except:
            pass
# create the DAG which calls the python logic that you had created above
default_dag_args = { 
    'start_date': datetime(2023, 4, 22), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=1), 
    'project_id': 1 }

# crontab notation can be useful https://crontab.guru/#0_0_*_*_1
with DAG("market_data_alphavantage_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:

# here we define our tasks
    task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data, op_kwargs = {'tickers' : list_of_stocks})    
    


