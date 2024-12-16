#### Step 1 : Project folder creation
Create project folder & navigate into it.
```python
mkdir pyspark
cd pyspark
```
----------------------------------------------------------------------------------------------------------
#### Step 2 : Creating docker-compose.yml
Create & open `docker-compose.yml` file.
```python
nano docker-compose.yml
```

Paste the below code & save.
```python
version: '3'
services:
  spark:
    image: jupyter/pyspark-notebook
    ports:
      - "8888:8888"  # Jupyter Notebook
      - "4040:4040"  # Spark UI
    volumes:
      - ./files/data:/home/jovyan/work/files/data
      - ./files:/home/jovyan/work/files
    environment:
      - JUPYTER_ENABLE_LAB=yes
    command: start.sh jupyter lab --NotebookApp.token=''

  spark-master:
    image: bitnami/spark:latest
    environment:
      - SPARK_MODE=master
    ports:
      - "8080:8080"
      - "7077:7077"

  spark-worker:
    image: bitnami/spark:latest
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
    depends_on:
      - spark-master
```
----------------------------------------------------------------------------------------------------------
#### Step 3 : Creating folders named files & data
Let's create folders named `files` to store jupyter notebook files & `data` folder to store the data which needs to be analyzed.
```python
mkdir files
mkdir data
```
----------------------------------------------------------------------------------------------------------
#### Step 4 : Let's create and start the container
By using `docker-compose.yml` file which we created, let's create the container & start it.
```python
docker-compose up
```
----------------------------------------------------------------------------------------------------------
