##### Note:
You need to keep snowflake passowrd here inside the code.</br>
OR</br>
Implement this using `.env` file.

----------------------------------------------------------------------------
Let's navigate to `/home/ubuntu/dags` & create file named `dag_code.py`</br>
Paste the below code inside this file.

```python
import logging
import airflow
from airflow import DAG
import snowflake.connector
from airflow.operators.python_operator import PythonOperator
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
				(101, 'B' ,5000, 300,'HEIDI_HR'),
				(102, 'C' ,6000, 400,'Sales'),
				(103, 'D' ,500, 50,'Sales'),
				(104, 'E' ,15000, 3000,'Tech'),
				(105, 'F' ,150000, 20050,'Tech'),
				(105, 'F' ,150000, 20060,'Tech');
	"""
]

# Function to execute the Snowflake query programmatically
def execute_snowflake_query(sql_query):
    # Directly create a connection to Snowflake using the Snowflake Python connector
    conn = snowflake.connector.connect(
		account = "OAYLMLL-AEB33440",
		user = "HEIDI",
		password = "Cooleuroscooleuros1!",
		role = "ACCOUNTADMIN",
		warehouse = "COMPUTE_WH",
		database = "RAMU",
		schema = "PUBLIC"
	)
    
    # Create a cursor and execute a SQL query
    cursor = conn.cursor()
    sql_query = sql_query
    cursor.execute(sql_query)
    
    # Fetch the result
    result = cursor.fetchone()
    print(f"Result: {result}")
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

# We created `dag` object already right?
with dag:
	create_table = PythonOperator(
        task_id="create_table",
        python_callable=execute_snowflake_query,
		op_kwargs={
            'sql_query': snowflake_query[0]
        }
    )
	insert_data = PythonOperator(
        task_id="insert_snowflake_data",
        python_callable=execute_snowflake_query,
		op_kwargs={
            'sql_query': snowflake_query[1]
        }
    )
		
# This is the order of DAG task's that will be run one after the other.
create_table >> insert_data
```
