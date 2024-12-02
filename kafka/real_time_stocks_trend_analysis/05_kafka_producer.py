# pip install kafka
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(
    bootstrap_servers=["54.227.123.170:9092"],  # change ip here
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)

producer.send("cricket", value={"Openers": "Rohit & Rahul"})
