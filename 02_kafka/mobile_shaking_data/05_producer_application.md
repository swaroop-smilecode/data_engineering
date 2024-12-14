#### Create an lambda fn
- Name as `mobile_shaking_data_producer`
- Layer of `kafka-python`
```python
mkdir python

pip install --platform manylinux2014_x86_64 --target=python --implementation cp --python-version 3.13 --only-binary=:all: --upgrade kafka-python -t "C:/Users/swaro/Desktop/python"
```
- Producer code</br>
  (Please observe that the public IP of EC2 has to be provided inside this code)
```python
import json
from time import sleep
from json import dumps
from kafka import KafkaProducer
import json

topic_name='sensor_data_consumer'
producer = KafkaProducer(bootstrap_servers=['44.197.178.172:9092']
,value_serializer=lambda x: dumps(x).encode('utf-8'))

def lambda_handler(event, context):
    # TODO implement
    print(event)
    payload_part=json.loads(event['body'])['payload']
    for i in payload_part:
        acc_x=i['values']['x']
        acc_y=i['values']['y']
        acc_z=i['values']['z']
        capture_time=i['time']
        data={"acc_x":acc_x,"acc_y":acc_y,"acc_z":acc_z,"capture_time":capture_time}
        print(data)
        producer.send(topic_name, value=data)
    producer.flush()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

- API gateway</br>
  Choose an API type : `REST API`</br>
  API name : `mobile_shaking_data_producer_gate_way`</br>
  API endpoint type : `Regional`</br>
  Create resource : `/mobile_shaking_data_producer`
  Create method :
                  Method type : `POST`
                  Integration type : `Lambda function`</br>
                  Lambda function : `mobile_shaking_data_producer`</br>
  Click on `Deploy API` button at top right corner --> Stage : `New stage` --> Stage name : `dev`</br>
  Invoke URL : `https://otlw56jph4.execute-api.us-east-1.amazonaws.com/dev/mobile_shaking_data_producer`
  
There is an andriod app named `Sensor Logger`. That's our producer application.</br>
<ins>step 1</ins></br>
Install `Sensor Logger` app
