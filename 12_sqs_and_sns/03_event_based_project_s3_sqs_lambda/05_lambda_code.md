This is what the below code does.
```python
import json

def lambda_handler(event, context):
    TODO implement
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
