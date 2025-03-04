```python
mkdir airflow-docker
cd airflow-docker

# Download docker yaml file for creating Airflow container
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'

mkdir ./dags ./logs ./config ./plugins

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

docker-compose up
```

You will see airflow running at below address, where `54.146.206.183` is the public ip address of EC2 instance.
```python
http://54.146.206.183:8080
```
Below are the default credentials to login into docker. These credentials are setup inside docker compose file. 
```python
airflow
airflow
```
