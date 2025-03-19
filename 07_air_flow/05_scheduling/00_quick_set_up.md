
<ins>This setup works in below situation:</ins></br>
You already installed docker in EC2 & then started running airflow container inside it.</br>
But, since it became evening; you wanted to shutdown the EC2 instance & then freshly start once again tomorrow just before you are about to start working.</br>

- Start EC2
- Connect to it
- Execute below commands:
  ```python
  sudo su
  cd airflow-docker
  echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  docker-compose up
  ```
- If you face any problems:
  ```python
  docker-compose down --volumes
  docker-compose up
  ```
- Below are the URL's at which Airflow & events_api will be running(Ofcourse, replace the IP by the EC2 instance IP).
  ```python
  http://3.237.252.35:8080
  http://3.237.252.35:5001/events
  ```
