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


# def add_step_emr(cluster_id, jar_file, step_args):
#     print("The cluster id : {}".format(cluster_id))
#     print("The step to be added : {}".format(step_args))
#     response = client.add_job_flow_steps(
#         JobFlowId=cluster_id,
#         Steps=[
#             {
#                 "Name": "test12",
#                 "ActionOnFailure": "CONTINUE",
#                 "HadoopJarStep": {"Jar": jar_file, "Args": step_args},
#             },
#         ],
#     )
#     print("The emr step is added")
#     return response["StepIds"][0]


# def get_status_of_step(cluster_id, step_id):
#     response = client.describe_step(ClusterId=cluster_id, StepId=step_id)
#     return response["Step"]["Status"]["State"]


# def wait_for_step_to_complete(cluster_id, step_id):
#     print("The cluster id : {}".format(cluster_id))
#     print("The emr step id : {}".format(step_id))
#     while True:
#         try:
#             status = get_status_of_step(cluster_id, step_id)
#             if status == "COMPLETED":
#                 break
#             else:
#                 print("The step is {}".format(status))
#                 sleep(40)

#         except Exception as e:
#             logging.info(e)


# def terminate_cluster(cluster_id):
#     try:
#         client.terminate_job_flows(JobFlowIds=[cluster_id])
#         logger.info("Terminated cluster %s.", cluster_id)
#     except ClientError:
#         logger.exception("Couldn't terminate cluster %s.", cluster_id)
#         raise


with dag:
    create_emr_cluster = PythonOperator(
        task_id="create_emr_cluster",
        python_callable=create_emr_cluster,
        dag=dag,
    )
#     poll_step_layer = PythonOperator(
#         task_id="poll_step_layer",
#         python_callable=wait_for_step_to_complete,
#         op_args=['{{ ti.xcom_pull("create_emr_cluster")["JobFlowId"]}}'],
#         dag=dag,
#     )
#     transform_layer = PythonOperator(
#         task_id="transform_layer",
#         python_callable=add_step_emr,
#         op_args=[
#             '{{ ti.xcom_pull("create_emr_cluster")["JobFlowId"]}}',
#             "command-runner.jar",
#             [
#                 "spark-submit",
#                 "--master",
#                 "yarn",
#                 "--deploy-mode",
#                 "cluster",
#                 "04_pyspark_code.py",
#             ],
#         ],
#         dag=dag,
#     )
#     poll_step_layer2 = PythonOperator(
#         task_id="poll_step_layer2",
#         python_callable=wait_for_step_to_complete,
#         op_args=[
#             '{{ ti.xcom_pull("create_emr_cluster")["JobFlowId"]}}',
#             '{{ ti.xcom_pull("transform_layer")}}',
#         ],
#         dag=dag,
#     )
#     terminate_emr_cluster = PythonOperator(
#         task_id="terminate_emr_cluster",
#         python_callable=terminate_cluster,
#         op_args=['{{ ti.xcom_pull("create_emr_cluster")["JobFlowId"]}}'],
#         dag=dag,
#     )

(create_emr_cluster)
