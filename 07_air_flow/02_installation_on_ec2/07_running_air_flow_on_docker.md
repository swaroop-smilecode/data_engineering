```python
mkdir airflow-docker
cd airflow-docker

# There is a file named docker-compose.yaml in this folder.
# copy that file into airflow-docker folder. 

mkdir ./dags ./logs ./config ./plugins

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

Let's start  the container based on yaml file.
```python
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

If you want to shutdown the container, then 
```python
docker-compose down
```
