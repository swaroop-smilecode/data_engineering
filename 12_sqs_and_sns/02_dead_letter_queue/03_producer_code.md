#### Publisher code
```python
pip install boto3
```
```python
import json
import boto3
import datetime
from datetime import date

# Create SQS client(`sqs_send`) using boto3 library,</br>
# so that this client we created will have respective methods to deal with SQS which is present inside AWS cloud.
sqs_send= boto3.client('sqs',  aws_access_key_id='{}',
aws_secret_access_key='{}', region_name='{}')

# Let's create an SQS from AWS UI --> Get the URL of that SQS & include in below code.
sendQueueUrl='{}'

# Prepare the message that needs to be send to SQS 
MessageAttributes={
    'Name': {
        'StringValue': 'Satadru Mukherjee',
        'DataType': 'String'
    },
    'Age': {
        'StringValue': '50',
        'DataType': 'Number'
    }}
# Observe here; i have wantedly removed }
# Why?
# Usually message is comunicated in JSON lang.
# Hence, as a first step, consumer tries to use the method json.loads to read the message which is in JSON format
# & store the result in variable.
# But, since the message is not in proper JSON format, the json.loads will fail
# This failure will be excepted in except block --> push this message to `dlqQueue` & delete from `sourceQueue`.
messageBody='''{"Name":"Satadru","Age":200'''

# Send message to SQS.
response = sendQueue(sendQueueUrl,messageBody,MessageAttributes)
```
