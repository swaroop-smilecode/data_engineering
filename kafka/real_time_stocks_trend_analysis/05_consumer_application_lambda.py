from kafka import KafkaConsumer
import json
import time
import boto3

consumer = KafkaConsumer("cricket", bootstrap_servers="3.91.5.89:9092")

for data in consumer:
    # Convert data to JSON
    data = data.value
    data_json = json.loads(data.decode("utf-8"))

    # Create file
    filename = "user_reg_data_" + time.strftime("%Y%m%d-%H%M%S") + ".json"
    with open(filename, "w") as outfile:
        json.dump(data_json, outfile)

    # # Upload the file
    # # s3_client = boto3.client('s3')
    # # response = s3_client.upload_file(file_name, bucket, object_name)
