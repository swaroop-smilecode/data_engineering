As shown in the architecture diagram, we need to start 3 servers.
1. Zoo keeper
2. Kafka cluster
3. Consumer
--------------------------------------------------------------------------------------------------------------------------------
#### Create EC2 instance(to run kafka & zoo keeper servers)
You need to take care of below things while creating EC2 instance. Rest everything can be left as default.</br>
- Key pair</br>
- Vpc</br>
- Public_subnet</br>
  (I am creating kafka server in public subnet for making the project in simple way. Ideally kafka server should be inside private subnet,</br>
   but again, establishing the communication etc. is a bit of work which will deviate from moto of this project which is not security.</br>
   `enable` auto assign public IP option, since you are creating instance inside public subnet)</br>
- Security_group</br>
  Allow all traffic from internet(Again, this is not who it should be. I am compromising).
  ![image](https://github.com/user-attachments/assets/cc770fa4-6897-4220-a6c4-30c81e2ef49d)

--------------------------------------------------------------------------------------------------------------------------------
#### Install kafka(zookeeper also get's installed) 
<ins>Install Java</ins></br>
Because kafka runs on top of Java, install java.
```python
sudo yum install java
```
<ins>Install kafka</ins>
```python
wget https://downloads.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz
tar -xvf kafka_2.12-3.9.0.tgz
```
--------------------------------------------------------------------------------------------------------------------------------
#### Start the servers 
<ins>Zoo keeper</ins>
- `cd kafka_2.12-3.9.0`
- `bin/zookeeper-server-start.sh config/zookeeper.properties`

<ins>Kafka server</ins>
- `cd kafka_2.12-3.9.0`
- `export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"`
- <ins>Changing kafka server properties to run it on public IP of EC2 instance</ins></br>
  Any computer will have 2 IP's(One public IP & one private IP). Similarly, our EC2 machine also will have one public IP & one private IP.</br>
  By default, kafka server runs on the private IP & you can't reach private IP from internet. Hence,</br>
  change server.properties so that it run's on public IP.</br>
  `sudo nano config/server.properties`</br>
  By default, one of the line in this file looks like `#advertised.listeners=PLAINTEXT://your.host.name:9092`</br>
  Uncomment the line & replace `your.host.name` with that of public IP of EC2 machine `54.227.123.170`</br>
  Save.
- <ins>Start the server</ins></br>
  `bin/kafka-server-start.sh config/server.properties`

--------------------------------------------------------------------------------------------------------------------------
#### Create topic in kafka server
- `cd kafka_2.12-3.9.0`
- `bin/kafka-topics.sh --bootstrap-server 54.227.123.170:9092 --topic mobile_shaking_data --create --partitions 1 --replication-factor 1`

--------------------------------------------------------------------------------------------------------------------------------
