After opening terminal through putty, execute below commands to install airflow server.
```python
sudo apt update

sudo apt install python3-pip

sudo apt install sqlite3

sudo apt-get install libpq-dev

pip3 install --upgrade awscli

sudo pip3 install virtualenv
virtualenv venv 
source venv/bin/activate

pip install "apache-airflow[postgres]==2.5.0" --constraint \
"https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"

pip install pandas apache-airflow-providers-snowflake==2.1.0 snowflake-connector-python==2.5.1 snowflake-sqlalchemy==1.2.5
pip install apache-airflow-providers-snowflake
pip install snowflake-connector-python
pip install snowflake-sqlalchemy

airflow db init

sudo apt-get install postgresql postgresql-contrib

sudo -i -u postgres

psql

CREATE DATABASE airflow;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

exit
exit

ls
cd airflow
sed -i 's#sqlite:////home/ubuntu/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg
sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg

airflow db init

airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com
# Above command is creating an user named `airflow` & at the middle of above command execution, it will ask you for password
password--admin@123!

mkdir /home/ubuntu/dags
# Now we need to edit file named `airflow.cfg`.
# But, since the editors like nano etc are difficult, let's use `winscp` & connect to our EC2 instacne.
# Through winscp, we can work on the files as if they are present at our local computer.
```
![image](https://github.com/user-attachments/assets/b566a89f-73d0-4675-b3dd-05f1ddbafd69)</br>
Note:</br>
Observe `SCP` protocol is used.
![image](https://github.com/user-attachments/assets/47a73aa1-702f-4f57-87cd-55f6a5019c2e)
```python
# After connecting to EC2 instance, navigate to the location /home/ubuntu/airflow/airflow.cfg
# Update below properties
dags_folder = /home/ubuntu/dags
load_examples = False
AIRFLOW__CORE__TEST_CONNECTION=Enabled
```

