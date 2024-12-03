from dotenv import load_dotenv
import os
from kafka import KafkaConsumer
import time
import boto3


consumer = KafkaConsumer("cricket", bootstrap_servers="3.91.5.89:9092")

# Get aws credentials from .env file
load_dotenv()

# boto3 session
session = boto3.Session(
    aws_access_key_id=os.getenv("aws_access_key_id"),
    aws_secret_access_key=os.getenv("aws_secret_access_key"),
)

s3_client = session.client("s3")
for data in consumer:
    # Convert data to JSON
    data = data.value

    s3 = boto3.resource("s3")

    # Store file in S3
    file_name = "user_reg_data_" + time.strftime("%Y%m%d-%H%M%S") + ".json"
    s3_client.put_object(Body=data, Bucket="streamed-data-heidi", Key=file_name)
