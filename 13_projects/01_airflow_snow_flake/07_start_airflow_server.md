You already had putty opened. Go there..</br>

---------------------------------------------------------------------------------------
Start airflow webserver
```python
airflow db init
airflow webserver
```
---------------------------------------------------------------------------------------
Once airflow webserver is started, duplicate the session & login: `ubuntu`
![image](https://github.com/user-attachments/assets/5858a9ab-527d-4e37-8f99-310b0e4afbb6)

---------------------------------------------------------------------------------------
Start airflow scheduler server
```python
# Activate python virtual environment.
source venv/bin/activate
# Start airflow `scheduler server`
airflow scheduler
```
---------------------------------------------------------------------------------------
