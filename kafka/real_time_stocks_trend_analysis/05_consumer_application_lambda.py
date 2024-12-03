from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("cricket", bootstrap_servers="3.91.5.89:9092")

for data in consumer:
    print("-----------------------------------------------------------------")
    print(data.value)
