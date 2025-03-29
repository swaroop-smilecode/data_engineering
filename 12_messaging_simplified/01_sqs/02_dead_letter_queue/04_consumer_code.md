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
