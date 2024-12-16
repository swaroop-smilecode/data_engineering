----------------------------------------------------------------------------------------------------------
#### Step 1 : Docker installation & starting the service</br>
To create docker image we need docker installed. That's what we are going to do now.</br>
- Create an EC2 instance named `docker_trending_youtube_videos_analysis`(free tier is good enough).
- When you connect to EC2 instance, by default you will be logged in as ec2-user. He doesn't have much powers,</br>
  hence, every time you need type `sudo` before the command. Let's switch to root user through below command.</br>
  ```python
  sudo su
  ```
  I dont know why, when you execute above command, you will not be inside the `~` folder. Hence do below.
  ```python
  cd ~
  ```
- Once the image is created, we want to push that image to `ECR` which is an aws service.</br>
  To do that, you(`you means, the user showed in command promt of EC2 machine`) need to have access to ECR.</br>
  For this purpose, let's configure aws credentials.</br>
  For configuring credentials, you need `awscli` & it comes by default with EC2 instance.</br>
  So, you no need to install it, just start using the awscli commands.
  ```python
  aws configure
  AWS Access Key ID [None]: <Keep your access key id here>
  AWS Secret Access Key [None]: <Keep your access key here>
  Default region name [None]: us-east-1
  Default output format [None]: press enter
  ```
- Install & start docker server.
  ```python
  yum install -y docker
  service docker start
  ```
----------------------------------------------------------------------------------------------------------
#### Step 2 : Project folder creation
Create project folder & navigate into it.
```python
mkdir pyspark
cd pyspark
```
----------------------------------------------------------------------------------------------------------
#### Step 3 : Creating docker-compose.yml
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
#### Step 4 : Creating folders named files & data
Let's create folders named `files` to store jupyter notebook files & `data` folder to store the data which needs to be analyzed.
```python
mkdir files
mkdir data
```
----------------------------------------------------------------------------------------------------------
