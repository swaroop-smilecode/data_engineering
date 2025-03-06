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
- If you look at DAG file, there will be below code which is used to create tmp/images path into which images will be downloaded.</br>
  But, this code seems not working. 
  ```python
  # Ensure directory exists
  pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)
  ```
  So, will create the required folders manually as below.</br>
  Create folder `tmp` 
  ```python
  mkdir tmp
  ```
  Navigate into `tmp` folder & create folder `images`
  ```python
  mkdir images
  ```
- Whenever you want to shutdown & start up docker containers. Below are the commands.
  ```python
  docker-compose down
  docker-compose up
  ```
