#### Architecture
I am not explaining this architecture, because it's self understandable by reading this picture.

![image](https://github.com/user-attachments/assets/35507299-71c3-471c-a273-213f94045b8a)

#### Consumer code
Think. Consumer is the one which polls for message --> Try to process it --> If processed, delete from SQS</br>
If could not able to process, then keep that message in DLQ & delete from original queue.

```python
pip install boto3
```
```python
import json
import boto3
import datetime
from datetime import date

# Get the source queue URL from AWS
# Get the dead letter queue URL from AWS
sourceQueueUrl=""
dlqQueueUrl=""

# Defining Custom Function to Send Message to Main Queue and Deleting it from DLQ 
def sendQueue(sendQueueUrl,messageBody,messageAttributes) :
    # Calling Send Message API
    ret = sqs_send.send_message( QueueUrl=sendQueueUrl, 
                            MessageBody=messageBody,
                            MessageAttributes=messageAttributes) 
    return ret
     
# All the below work is done by this consume_message() method.
# Poll for 10 messages from `sourceQueue`
# try:
#   Loop through each message & do some work
# except Exception as e:
#            Send this message to dlqQueue
#            Delete this message from sourceQueue
def consume_message():
  messages = sqs_send.receive_message(QueueUrl=sourceQueueUrl, MaxNumberOfMessages=10
                                    ,WaitTimeSeconds=20,MessageAttributeNames=['All'])
  if 'Messages' in messages:
    for m in messages['Messages']:
      print(m)
      MessageAttributes=m['MessageAttributes']
      messageBody=m['Body']
      try:
        msg_body=json.loads(messageBody)
      except Exception as e:
        print(e)
        sqs_send.send_message(QueueUrl = dlqQueueUrl, MessageBody = messageBody, MessageAttributes = MessageAttributes)
        sqs_send.delete_message(QueueUrl = sourceQueueUrl, ReceiptHandle = m['ReceiptHandle'])
consume_message()
```
#### Put Failed Events back to Source Queue
```python
pip install boto3
```
```python
import json
import boto3
import traceback
import datetime
from datetime import date

# Month abbreviation, day and year
today = date.today()	
d4 = today.strftime("%b-%d-%Y")

# Look at the architecture diagram
# We need to deal with two kind of AWS services
# 1. SQS
# 2. S3(Even after multiple retries, if the message is not processed,
#       will store that message in s3 bucket & make sure that it is not present either in source_sqs OR dlq_sqs)
# So, will create clients for those 2 services using boto3
sqs_client=boto3.client('sqs',  aws_access_key_id='',
aws_secret_access_key='', region_name='us-east-2')

s3= boto3.client('s3',aws_access_key_id='',
aws_secret_access_key='', region_name='us-east-2')

# Assign values to variables in below code.
sqs_dlq= ""
sqs_source_queue=""
s3_prefix_stage=''
s3_bucket=""
max_retries=
```
