- Let's create a folder named `airflow-docker` inside which will keep all things needed to create airflow container(`docker-compose.yaml`) &</br>
  run that container(dags folder, logs folder, config folder & plugins folder).
  ```python
  mkdir airflow-docker
  cd airflow-docker
  ```
- There is a file named `docker-compose.yaml` in this folder.</br>
  Copy that file into airflow-docker folder using WinSCP. 
- Create folders named dags, logs, config, plugins
  ```python
  mkdir ./dags ./logs ./config ./plugins
  ```
- Below command needs to be executed. I don't know why :)
  ```
  echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ```
- Let's start airflow container.
  ```python
  docker-compose up
  ```
- You will see airflow running at below address, where `54.146.206.183` is the public ip address of EC2 instance.
  ```python
  http://54.146.206.183:8080
  ```
  Note:</br>
  Below are the default credentials to login into docker. These credentials are setup inside docker compose file. 
  ```python
  airflow
  airflow
  ```
  Note:</br>
  If you want to shutdown the container, then 
  ```python
  docker-compose down
  ```
