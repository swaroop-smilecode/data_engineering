- Let's create a folder named `airflow-docker` inside which will keep all things needed to create airflow container(through the help of `docker-compose.yaml`).
  ```python
  mkdir airflow-docker
  cd airflow-docker
  ```
- There is a file named `docker-compose.yaml` in this folder.</br>
  Copy that file into airflow-docker folder using WinSCP. 
- Create folders named dags, logs, config, plugins. The question is why?</br>
  - Whenever you want to interact with any software which is running through docker container(for ex: airflow in this case),</br>
    you need to find the container number of airflow(airflow will start many containers, but especially you need `web_server_1` container)</br>
    & then execute below command.
    ```python
    docker exec -it --user root 3397acbc004a bash
    ```
  - To avoid this, we map folders from inside the airflow container to linux environment which is local environment to us.</br>
    For example; DAG files need to be created in the dags folder present inside the container. So, instead of logging into container</br>
    each & every time, then copying the DAG file, just place the DAG file in the dags folder present at your local environment</br>
    it gets copied to the dags folder of docker automatically since we mapped these fodlers thorugh volumes. 
    ```python
    mkdir ./dags ./logs ./config ./plugins ./output
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
