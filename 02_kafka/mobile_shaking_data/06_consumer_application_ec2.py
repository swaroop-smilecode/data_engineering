from kafka import KafkaConsumer
from kafka import TopicPartition, OffsetAndMetadata
import json


consumer = KafkaConsumer(
    "mobile_shaking_data_1",
    bootstrap_servers=["34.200.238.108:9092"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    group_id="acceleration_test",
    auto_offset_reset="earliest",
    enable_auto_commit=False,
)


for message in consumer:
    data = message.value
    x_accl = data["acc_x"]
    y_accl = data["acc_y"]
    z_accl = data["acc_z"]
    mag = abs(x_accl) + abs(y_accl) + abs(z_accl)
    if mag >= 15:
        print("*" * 100)
        print("Shaking")
        print("*" * 100)
    else:
        print("Idle")
    tp = TopicPartition(message.topic, message.partition)
    om = OffsetAndMetadata(message.offset + 1, message.timestamp)
    consumer.commit({tp: om})
