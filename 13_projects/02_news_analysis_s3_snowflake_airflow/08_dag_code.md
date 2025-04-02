Save the file at `/home/ubuntu/dags`</br>
There is a variable named password in the below code, which holds snowflake password. Assign password value to that variable.

# Include below things before running the code. 
- snowflake.connector.connect(password="<>")
- 

#### dag_code.py
```python
import logging
import airflow
from airflow import DAG
import snowflake.connector
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from news_fetcher_py import runner
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


args = {"owner": "Airflow", "start_date": airflow.utils.dates.days_ago(2)}

dag = DAG(
    dag_id="snowflake_automation_dag", default_args=args, schedule_interval=None
)


# Function to execute the Snowflake query programmatically
def execute_snowflake_query(sql_query):
    # Directly create a connection to Snowflake using the Snowflake Python connector
    conn = snowflake.connector.connect(
		account = "OAYLMLL-AEB33440",
		user = "HEIDI",
		password = "",
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


with dag:

	extract_news_info = PythonOperator(
		task_id='extract_news_info',
		python_callable=runner,
		dag=dag, 
		)
		
	move_file_to_s3 = BashOperator(
		task_id="move_file_to_s3",
		bash_command='aws s3 mv {{ ti.xcom_pull("extract_news_info")}}  s3://irisseta-heidi',
		)

	snowflake_create_table = PythonOperator(
        	task_id="snowflake_create_table",
        	python_callable=execute_snowflake_query,
            	op_kwargs={
            	'sql_query': """create  table if not exists helloparquet 
                            	using template(select ARRAY_AGG(OBJECT_CONSTRUCT(*)) 
				from TABLE(INFER_SCHEMA (LOCATION=>'@ramu.PUBLIC.snow_simple',FILE_FORMAT=>'parquet_format')))
                            """ 
                         }
    		)

	snowflake_copy = PythonOperator(
        	task_id="snowflake_copy",
        	python_callable=execute_snowflake_query,
		op_kwargs={
            	'sql_query': """copy into ramu.PUBLIC.helloparquet 
		       		from @ramu.PUBLIC.snow_simple 
			   	MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE 
			   	FILE_FORMAT=parquet_format
                             """
			}
    		)
	

extract_news_info >> move_file_to_s3 >> snowflake_create_table >> snowflake_copy
```
