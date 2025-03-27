Let's navigate to `/home/ubuntu/dags` & create file named `dag_code.py`</br>
Paste the below code inside this file.

```python
import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# `owner` is owner of the DAG
# `start_date` is when the DAG should run for the first time. 
# Then onwards, DAG will run as per schedule.
args = {"owner": "Airflow", "start_date": airflow.utils.dates.days_ago(2)}

# Creation og dag object
# `dag_id` is DAG name
dag = DAG(
    dag_id="snowflake_automation_dag", default_args=args, schedule_interval=None
)

# Below are the two queries which we will be executing in snowflake.
# Observe that we are creating an array & storing the queries inside this this array.
# Later, will refer to these queries with the help of array indexes.
snowflake_query = [
	"""
	    create  table if not exists source_table( emp_no int,emp_name text,salary int, hra int ,Dept text);
	""",
	"""INSERT INTO source_table VALUES (100, 'A' ,2000, 100,'HR'),
				(101, 'B' ,5000, 300,'HR'),
				(102, 'C' ,6000, 400,'Sales'),
				(103, 'D' ,500, 50,'Sales'),
				(104, 'E' ,15000, 3000,'Tech'),
				(105, 'F' ,150000, 20050,'Tech'),
				(105, 'F' ,150000, 20060,'Tech');
	"""
]

# Get connection to snow_flake
import snowflake.connector as sf
conn_object = sf.connect(
account = "OAYLMLL-AEB33440",
user = "HEIDI",
password = "Cooleuroscooleuros1!",
role = "ACCOUNTADMIN",
warehouse = "COMPUTE_WH",
database = "RAMU",
schema = "PUBLIC"
)

# We created `dag` object already right?
with dag:
	create_table = SQLExecuteQueryOperator(
			task_id="create_table",
			sql=snowflake_query[0],
			conn_id = "snowflake_conn"
		)		
	insert_data = SQLExecuteQueryOperator(
		task_id="insert_snowflake_data",
		sql=snowflake_query[1],
                conn_id = "snowflake_conn"
	)
# This is the order of DAG task's that will be run one after the other.
create_table >> insert_data
```
