- But, we don't have e-commerce website in reality.</br>
- So, what will do is, will create an api that will provide us 30 days data which says : on so & so date, this particular user visited these pages.</br>
  Will develop this API using Flask framwework & Flask server will be run as an container.</br>
  Look at `docker/events-api` folder.</br>
  It contains app.py, which is nothing but Flask app.</br>
  Then there is also an Docker file. That's for running Flask app in a container.</br>
- Now, look at the end of `docker-compose.yaml` file, where you will see below code.
  ```python
  events_api:
  build: ./docker/events-api
  image: manning-airflow/events-api
  ports:
    - "5001:5000"
  ```
  So, think like this: docker-compose.yaml file is the single file with the help of which you are going to create 2 containers named ariflow & Flask API.</br>
  But, here is the important point.</br>
  The code which is required to create an airflow container is present in the docker-compsoe.yaml file itself. Where as the code required to create
  Flask container is present at `docker\events-api\Dockerfile`.
  ```python
  curl -o /tmp/events.json http://localhost:5000/events
  ```
- Will create this api providing server through an docker container.</br>
  To do that: as a first step, copy `events-api` folder present here into `airflow-docker` folder present inside the EC2 insatnce.</br>
  Then run below command to create image named `event-api`.
  ```python
  docker build -t event-api .
  ```
  Then, execute below command to start the container based on the `events-api` image.</br>
  Here, `5001` is the port on host & `5000` is the container post.</br>
  This is how to remember. Host(House) is the first thing to be there inorder to host others inside the it.</br>
  Hence, port number that comes first is the host port.
  ```python
  docker run -p 5001:5000 event-api
  ```
  Once container is started, if you hit the below address, you will receive data.
  ```python
  http://44.205.3.218:5001/events
  ```
- Let's navigate to below location & create dag file named `website_event.py`. This is our new dag(name of the dag is `01_unscheduled`).
  ```python
  /home/ec2-user/airflow-docker/dags
  ```
  It will take some time to see the DAG in airflow website.</br>
  Wait & if you don't see yet, then restart docker in which airflow is runnning by using `docker-compose down`.
  
