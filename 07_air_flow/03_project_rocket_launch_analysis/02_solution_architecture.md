- Install docker software, then run airflow container inside that docker. This is the setup required for project &</br>
  it's clearly explained in `02_installation_on_ec2` folder.
- Inside airflow container, we need to create folder structure `tmp/images` in which will store the downloaded images.</br>
  To do that, first execute `docker ps`, which will list all the containers that are running currently.</br>
  Airflow starts multilpe containers. Among them, pick up `web_server_1` container id(Ex: 3397acbc004a).</br>
  Execute below command so that you will be inside `web_server_1` container.</br>
  ```python
  docker exec -it --user root 3397acbc004a bash
  ```
  To exit from docker & go back to your host location:
  ```python
  exit
  ```
-  Let's create folder structure
    ```python
    mkdir tmp
    ```
    Navigate into `tmp` folder & create folder `images`
    ```python
    mkdir images
    ```
- If you check `docker-compose.yaml` file, we mapped `/tmp` to `/output` in our local environment.</br>
  So, once the running of DAG is completed, you can see downloaded images inside the output folder in your local environment.
