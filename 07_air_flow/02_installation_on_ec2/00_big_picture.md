- Before you want to run software with the help of docker. First of all, docker software should be running inside the linux server.
- So, first step would be to install docker inside our linux enviroment.
  ![image](https://github.com/user-attachments/assets/bb5cf88e-bee7-4f65-8347-25170f80b538)
- Then, 
- Whenever you want to interact with any software which is running through docker container(for ex: airflow in this case),</br>
  you need to find the container number of airflow(airflow will start many containers, but especially you need `web_server_1` container) &</br>
  then execute below command.
  ```python
  docker exec -it --user root 3397acbc004a bash
  ```
- To avoid this, we map folders from inside the airflow container to linux environment which is local environment to us.</br>
  For example; DAG files need to be created in the dags folder present inside the container. So, instead of logging into container</br>
  each & every time, then copying the DAG file, just place the DAG file in the dags folder present at your local environment</br>
  it gets copied to the dags folder of docker automatically since we mapped these fodlers thorugh volumes.
  ![image](https://github.com/user-attachments/assets/31566f21-d585-44ad-8356-45880e287054)
