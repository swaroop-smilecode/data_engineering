# Get env variables from .env file
# ------------------------------------------------------------#
from dotenv import load_dotenv
import os

load_dotenv()

aws_access_key_id_env = os.getenv("aws_access_key_id")
aws_secret_access_key_env = os.getenv("aws_secret_access_key")
Ec2KeyName_env = os.getenv("Ec2KeyName")
Ec2SubnetId_env = os.getenv("Ec2SubnetId")
LogUri_env = os.getenv("LogUri")
# ------------------------------------------------------------#

import boto3
import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from time import sleep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

args = {"owner": "Airflow", "start_date": airflow.utils.dates.days_ago(2)}

dag = DAG(dag_id="snowflake_automation_dag", default_args=args, schedule_interval=None)

client = boto3.client(
    "emr",
    region_name="us-east-1",
    aws_access_key_id=aws_access_key_id_env,
    aws_secret_access_key=aws_secret_access_key_env,
)


def create_emr_cluster():
    cluster_id = client.run_job_flow(
        Name="transient_demo_testing",
        Instances={
            "InstanceGroups": [
                {
                    "Name": "Master",
                    "Market": "ON_DEMAND",
                    "InstanceRole": "MASTER",
                    "InstanceType": "m1.xlarge",
                    "InstanceCount": 1,
                },
                {
                    "Name": "Slave",
                    "Market": "ON_DEMAND",
                    "InstanceRole": "CORE",
                    "InstanceType": "m1.xlarge",
                    "InstanceCount": 2,
                },
            ],
            "Ec2KeyName": Ec2KeyName_env,
            "KeepJobFlowAliveWhenNoSteps": True,
            "TerminationProtected": False,
            "Ec2SubnetId": Ec2SubnetId_env,
        },
        LogUri=LogUri_env,
        ReleaseLabel="emr-5.33.0",
        BootstrapActions=[],
        VisibleToAllUsers=True,
        JobFlowRole="EMR_EC2_DefaultRole",
        ServiceRole="EMR_DefaultRole",
        Applications=[{"Name": "Spark"}, {"Name": "Hive"}],
    )
    print("The cluster started with cluster id : {}".format(cluster_id))
    return cluster_id
