----------------------------------------------------------------------------------------------------------
#### Let's start action 
<ins>Step 1 :</ins> Docker installation & starting the service</br>
To create docker image we need docker installed. That's what we are going to do now.</br>
- Create an EC2 instance named `docker_trending_youtube_videos_analysis`(free tier is good enough).
- When you connect to EC2 instance, by default you will be logged in as ec2-user. He doesn't have much powers,</br>
  hence, every time you need type `sudo` before the command. Let's switch to root user through below command.</br>
  ```python
  sudo su
  ```
  I dont know why, when you execute above command, you will not be inside the `~` folder. Hence do below.
  ```python
  cd ~
  ```
- Once the image is created, we want to push that image to `ECR` which is an aws service.</br>
  To do that, you(`you means, the user showed in command promt of EC2 machine`) need to have access to ECR.</br>
  For this purpose, let's configure aws credentials.</br>
  For configuring credentials, you need `awscli` & it comes by default with EC2 instance.</br>
  So, you no need to install it, just start using the awscli commands.
  ```python
  aws configure
  AWS Access Key ID [None]: <Keep your access key id here>
  AWS Secret Access Key [None]: <Keep your access key here>
  Default region name [None]: us-east-1
  Default output format [None]: press enter
  ```
- Install & start docker server.
  ```python
  yum install -y docker
  service docker start
  ```
  ----------------------------------------------------------------------------------------------------------
