from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("cricket", bootstrap_servers="54.227.123.170:9092")

for data in consumer:
    print("-----------------------------------------------------------------")
    print(data.value)
