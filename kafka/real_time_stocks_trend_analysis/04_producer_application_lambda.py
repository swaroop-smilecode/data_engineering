# pip install kafka-python-ng
# pip install faker
from faker import Faker
from kafka import KafkaProducer
import json
from time import sleep

fake = Faker()


def get_registered_user_data():
    data = {
        "name": fake.name(),
        "address": fake.address(),
        "registered_in_year": fake.year(),
    }
    data_json = json.dumps(data).encode("utf-8")
    return data_json


producer = KafkaProducer(bootstrap_servers=["3.91.5.89"])  # change ip here

while True:
    producer.send("cricket", value=get_registered_user_data())
    sleep(4)
