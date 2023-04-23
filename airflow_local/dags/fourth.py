import time 
import json 
from airflow import DAG 
from airflow.operators.postgres_operator import PostgresOperator 
from datetime import timedelta

from airflow.utils.dates import days_ago

default_args = { 'owner': 'airflow',
                'retries': 1, 
                'retry_delay': timedelta(minutes=5), 
                }

# Write a DAG which creates an employe table - each row represents a new person and contains info about their name and age
# then insert 3 people (with the correct metadata)
# finally execute a query which calculates the average age of all employees
create_query = """ 
DROP TABLE IF EXISTS develhope_test.employee_table
CREATE TABLE develhope_test.employee_table (id INT NOT NULL, employee_name VARCHAR(250) NOT NULL, age INT NOT NULL )
"""

# create a logic that populates the table with some data
insert_data_query = """
INSERT INTO develhope_test.employee_table (id, employee_name, age)
values(1, Onur, 35), (2, Ahmed,32), (3, Abdullah, 33)
"""

calculating_averag_age = """
SELECT AVG(age) as 'Age Avg' FROM develhope_test.employee_table """

dag_postgres = DAG(dag_id = "postgres_dag_connection", default_args = default_args, schedule_interval = None, start_date = days_ago(1))

# here you will define the tasks by calling the operator
create_table = PostgresOperator(task_id = "creation_of_table", sql = create_query, dag = dag_postgres, postgres_conn_id = "develhope_test.employee_table")

insert_data = PostgresOperator(task_id = "insertion_of_data", sql = insert_data_query, dag = dag_postgres, postgres_conn_id = "develhope_test.employee_table")

avg_data = PostgresOperator(task_id = "calculating_averag_age", sql = calculating_averag_age, dag = dag_postgres, postgres_conn_id = "develhope_test.employee_table")

create_table >> insert_data >> avg_data