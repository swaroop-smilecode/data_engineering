# Will break our dag workflow into two separate tasks:
# One for fetching user events(data) and another for calculating the statistics
from datetime import datetime
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Define the start date for the DAG
# Here, we are saying that this is an unscheduled DAG
dag = DAG(
    dag_id="01_unscheduled", start_date=datetime(2019, 1, 1), schedule_interval=None
)

# Fetch and store the events by hitting an API
fetch_events = BashOperator(
    task_id="fetch_events",
    # This is what bash_command is doing:
    # Making directory /data/events
    # Hitting http://events_api:5000/events
    # Storing the results in /data/events.json
    bash_command=(
        "mkdir -p /data/events && "
        "curl -o /data/events.json http://events_api:5000/events"
    ),
    dag=dag,
)


# This fn is accepting 2 arguments input_path & output_path
# input_path is the location where the data that need's to be analyzed is present
# output_path is the location where the analyzed data is stored
def _calculate_stats(input_path, output_path):
    """Calculates event statistics."""
    # Check output_path is present or not. If not, then make it
    Path(output_path).parent.mkdir(exist_ok=True)

    # Read the input data which is in json format
    events = pd.read_json(input_path)
    # This is the analysis that you are doing
    # Just group by date & user :)
    stats = events.groupby(["date", "user"]).size().reset_index()
    # Write the analyzed data(csv format) at output_path.
    stats.to_csv(output_path, index=False)


# You defined fn named _calculate_stats
# Now you have to call that fn, right?
# For that you need PythonOperator
calculate_stats = PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    op_kwargs={"input_path": "/data/events.json", "output_path": "/data/stats.csv"},
    dag=dag,
)

# This tells that first fetch_events(which is nothing but BashOperator) should run &
# Then, calculate_stats(PythonOperator) needs to be run.
fetch_events >> calculate_stats
