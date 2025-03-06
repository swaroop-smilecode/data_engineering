- `airflow-docker` is the folder inside which we keep `docker-compose.yaml` file, to create airlfow container & </br>
  the folders you see in below picture named `plugins`, `logs`, `dags`, `config` are the folders at our local environment(NOT inside docker)</br>
  we mapped these folders to the folders which are present inside airflow container.
- DAG file(`rocket_launch_analysis_dag.py`) needs to be placed inside `dags` folder which is present inside the container.</br>
  But, since you mapped folders which are inside the container to local environment, you can just place the DAG in</br>
  `dags` folder of local environment & that gets copied into the `dags` folder inside the container.
![image](https://github.com/user-attachments/assets/d632adfb-3245-4b2c-acbb-b6b4c49d4eda)
- For any reason, if you want to go into docker, then:</br>
  execute `docker ps`, which will list all the containers that are running currently.</br>
  Among them, pick up `web_server_1` container id(Ex: 3397acbc004a).</br>
  Execute below command so that you will be inside `web_server_1` container.</br>
  ```python
  docker exec -it --user root 3397acbc004a bash
  ```
  To exit from docker & go back to your host location:
  ```python
  exit
  ```
