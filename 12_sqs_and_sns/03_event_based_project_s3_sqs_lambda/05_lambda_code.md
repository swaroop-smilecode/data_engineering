Let me explain this lambda code.</br>

We know that, message is sent from SQS to lambda.</br>
This message is performing 2 duties</br>
    1. Triggering lambda</br>
    2. Acts as input for lambda code(`event` object)</br>

All that this lambda code doing is just extracting required data from `event` object & printing it.</br>
That printed information can be seen in cloud watch logs.

```python
import json

def lambda_handler(event, context):
    print(event)
    try:
        for i in event['Records']:
            s3_event = json.loads(i['body'])
            if 'Event' in s3_event and s3_event['Event'] == 's3:TestEvent':
                print("Test Event")
            else:
                for j in s3_event['Records']:
                    print("Bucket Name : {} ".format(j['s3']['bucket']['name']))
                    print("Object Name : {} ".format(j['s3']['object']['key']))
    except Exception as exception:
        print(exception)
```
