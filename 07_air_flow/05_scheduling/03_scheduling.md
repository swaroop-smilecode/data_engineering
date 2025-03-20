##### DAG without scheduling
```python
from datetime import datetime
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="01_unscheduled", start_date=datetime(2019, 1, 1), schedule_interval=None
)

fetch_events = BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /tmp/data && "
        "curl -o /tmp/data/events.json http://3.237.252.35:5001/events"
    ),
    dag=dag,
)

def _calculate_stats(input_path, output_path):
    """Calculates event statistics."""

    Path(output_path).parent.mkdir(exist_ok=True)

    events = pd.read_json(input_path)
    stats = events.groupby(["date", "user"]).size().reset_index()

    stats.to_csv(output_path, index=False)

calculate_stats = PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    op_kwargs={
        "input_path": "/tmp/data/events.json",
        "output_path": "/tmp/data/stats.csv",
    },
    dag=dag,
)

fetch_events >> calculate_stats
```

##### DAG scheduled daily
- Airflow provides convenient macro named `@daily` to run the DAG once every day at midnight.
- For below provided example; i tried to show when the DAG will be run(You need to observe that, even through you defined start date as 2019-01-01,
  first execution happens on 2019-01-02 00:00). That's how Airflow works.
  ```python
  dag = DAG(
      dag_id="03_with_end_date",
      start_date=datetime(2019, 1, 1),
      end_date=datetime(2019,1,5),
      schedule_interval='@daily'
  )
  ```
  ![image](https://github.com/user-attachments/assets/693a44ec-4537-46d2-9414-0c615eb162a8)

##### DAG scheduled based on corn job
- What if we want to run our jobs on hourly or weekly intervals?</br>
  And what about more complicated intervals in which we may want to run our DAG at 23:45 every Saturday?
- To support more complicated scheduling intervals,</br>
  Airflow allows us to define scheduling intervals using the same syntax as used by cron,</br>
  a time-based job scheduler used by Unix-like computer operating systems such as macOS and Linux.

##### DAG scheduled based on frequency based intervals
- You can't define cron job based on frequency based intervals. Hence the need of frequency based intervals.
- Example: Below code makes the DAG run once / 3 days.
  ```python
  dag = DAG(
    dag_id="04_time_delta",
    schedule_interval=datetime.timedelta(days=3),
    start_date=datetime(year=2019, month=1, day=1),
    end_date=datetime(year=2019, month=1, day=5)
  )
  ```
