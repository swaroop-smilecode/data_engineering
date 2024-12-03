from kafka import KafkaConsumer
import json
import time
import boto3

consumer = KafkaConsumer("cricket", bootstrap_servers="3.91.5.89:9092")

s3_client = boto3.client("s3")
for data in consumer:
    # Convert data to JSON
    data = data.value

    # Store file in S3
    file_name = "user_reg_data_" + time.strftime("%Y%m%d-%H%M%S") + ".json"
    s3_client.put_object(Body=data, Bucket="streamed-data-heidi", Key=file_name)
