from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import os
from datetime import datetime, timedelta
import json
import pandas as pd
import numpy as np



API_key="f679f0fb96a62d4e095329b6d7de7d07"


url="http://api.openweathermap.org/data/2.5/forecast?id=524901&appid="+API_key
r=requests(url)
data=r.json()

data
