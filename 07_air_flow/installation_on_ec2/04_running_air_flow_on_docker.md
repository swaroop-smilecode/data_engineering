```python
mkdir air_flow
cd air_flow

# Download docker yaml file
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'

mkdir ./dags ./logs ./config ./plugins

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up
```

You will see airflow running at below address
```python
http://54.146.206.183:8080
```
