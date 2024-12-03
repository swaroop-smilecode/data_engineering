--------------------------------------------------------------------------------------------------------------------------------
#### Overview.
- In file name, i wrote zk. It means zoo keeper.
- There is no separate installation needed for Zoo keeper. It comes along with kafka installation.
- As shown in the architecture diagram, we need to start 4 servers.
  1. Zoo keeper
  2. Kafka cluster
  3. Producer
  4. Consumer
- Think 🤔</br>
  You can't start kafka server on `lambda`, because it needs to consume messages & broadcast them continuously.</br>
  Where as lambda will stop it's work in some time.
- So, this is what we are going to do.</br>
  <ins>Step 1</ins></br>
  Install kafka server on EC2(linux OS). Zoo keeper also get's installed along with it.</br>
  After installation, will start Zoo keeper server first & then kafka server on same EC2 instance, but on different ports.</br>
  <ins>Step 2</ins></br>
  Then, will create an application named `register_user_application` on another EC2 instance. That's the producer.</br>
  <ins>Step 3</ins></br>
  Atleast will create an application named `data_analysis_application` on another EC2 instance. That's the consumer.</br>
  This application is the data pipeline.
- Will be running 4 servers which means, we also need to open 4 `cmd`'s</br>
  Since we created EC2 instance in public seubnet, we can directly connect to it through cmd provided by aws itself.</br>
  It's a simple process, since there is no need to provide key pair for authntication.
--------------------------------------------------------------------------------------------------------------------------------
#### Create EC2 instance(linux OS)
- You need to take care of below things while creating EC2 instance. Rest everything can be left as default.</br>
  key pair</br>
  vpc</br>
  subnet</br>
  `enable` auto assign public IP option, since you are creating instance inside public subnet.</br>
  security_group</br>
- While creating instance, you need to associate an key pair with the instance.</br>
  For example, let's consider that you created a key pair named `ec2-key-pair.pem`.</br>
  The moment you create this key pair, one key is downloaded into your laptop. Keep it safe, that's needed to login into EC2 machine.
- Create this instance in public subnet.</br>
  Reason is, producers & consumers will connect to kafka server running inside this instance, through internet.</br>
  Also, since you are creating EC2 in public subnet, `enable` auto assign public IP option.
--------------------------------------------------------------------------------------------------------------------------------
#### Changes needed to security group associated with EC2 instance
- Let's consider you want to connect to EC2 machine from `cmd`.</br>
  You can do this by executing command `ssh -i "ec2-key-pair.pem" ec2-user@ec2-54-227-123-170.compute-1.amazonaws.com`</br>
  This command is trying to establish connection to EC2 machine through ssh protocol.</br>
  So, there should be an inbound rule in security group associated with EC2 instance, to allow traffic using ssh protocol.
- Once you start the kafka server inside this EC2 machine, we dont know with which protocol, producers & servers will be connecting to it.</br>
  hence, create one more rule to allow all traffic.
  ![image](https://github.com/user-attachments/assets/0eab5a56-be57-46b6-9335-7c24898d0d06)

--------------------------------------------------------------------------------------------------------------------------------
#### Let's connect to EC2 instance.
- Open `cmd`.
- Previously we talked about an key pair will get downloaded into your computer. Navigate to that location & execute below command.</br>
  Replace the IP address shown in below command with that of IP address of EC2 machine.</br>
  `ssh -i "ec2-key-pair.pem" ec2-user@ec2-54-227-123-170.compute-1.amazonaws.com`</br>
- That's it. You get connected to EC2 machine.
--------------------------------------------------------------------------------------------------------------------------------
#### Download kafka
Download below binary file.</br>
`wget https://downloads.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz`

#### Unzip kafka
Binary files need not to be installed explicitly. Just un zipping is enough.</br>
`tar -xvf kafka_2.12-3.9.0.tgz`

--------------------------------------------------------------------------------------------------------------------------------
#### Install Java
Because kafka runs on top of Java, install java.</br>
`sudo yum install java`

--------------------------------------------------------------------------------------------------------------------------------
#### Start zoo keeper:
- `cd kafka_2.12-3.9.0`
- `bin/zookeeper-server-start.sh config/zookeeper.properties`

--------------------------------------------------------------------------------------------------------------------------------
#### Start Kafka server:
- Open new tab in cmd
- Again connect to EC2 machine
- `cd kafka_2.12-3.9.0`
- `export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"`
- <ins>Changing kafka server properties to run it on public IP of EC2 instance</ins></br>
  Any computer will have 2 IP's(One public IP & one private IP). Similarly, our EC2 machine also will have one public IP & one private IP.</br>
  By default, kafka server runs on the private IP & you can't reach private IP from internet. Hence,</br>
  change server.properties so that it run's on public IP.</br>
  `sudo nano config/server.properties`</br>
  By default, one of the line in this file looks like `#advertised.listeners=PLAINTEXT://your.host.name:9092`</br>
  Uncomment the line & replace `your.host.name` with that of public IP of EC2 machine `54.227.123.170`</br>
  `ctrl + x`</br>
  `y`</br>
  `Enter`
- <ins>Start the server</ins></br>
  `bin/kafka-server-start.sh config/server.properties`

--------------------------------------------------------------------------------------------------------------------------------
#### Note
zoo keeper server has to be started before starting kafka server.

--------------------------------------------------------------------------------------------------------------------------------
#### Create the topic:
- Open new tab in cmd
- Again connect to EC2 machine
- `cd kafka_2.12-3.9.0`
- `bin/kafka-topics.sh --bootstrap-server 54.227.123.170:9092 --topic cricket --create --partitions 1 --replication-factor 1`

--------------------------------------------------------------------------------------------------------------------------------
#### Note
Once EC2 instance is started, you will know public IP of instance, right?</br>
That address need to be placed at 3 locations.
1. `sudo nano config/server.properties`
2. `04_producer_application_lambda`
3. `05_consumer_application_lambda`

--------------------------------------------------------------------------------------------------------------------------------
