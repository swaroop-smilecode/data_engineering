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

# I need this d4 later in the code to create `s3_key`
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
sqs_dlq = "<url_of_dlq>"
sqs_source_queue = "<url_of_sqs>"
s3_prefix_stage = "unprocessedmessages"
                  # folder_path_starting_from_bucket_name.
                  # Yes, just from bucket name, it's enough.
                  # Since bucket name is unique one across the wolrd,
                  # AWS knows how to find your bucket even if you just specify the bucket name>"
s3_bucket="redrivepurge"
max_retries=2

# Function to send message to main queue and deleting it from dlq 
def sendAndDeleteQueue(sendQueueUrl,messageBody,messageAttributes,recieveQueueUrl,receiptHandle) :
    # Calling Send Message API
    ret = sqs_client.send_message(QueueUrl=sendQueueUrl, 
                                  MessageBody=messageBody,
                                  MessageAttributes=messageAttributes) 
                            
    # Calling Delete Message API 
    sqs_client.delete_message(QueueUrl=recieveQueueUrl,
                              ReceiptHandle=receiptHandle)

# The code present in this function, should ideally be inside lambda pointed at the picture pasted below
# Now, how to understand this code?
# See the text in architecture diagram. I have explained neatly
# Whatever is there, we just converted into code
def process_sqs_message(sqs_source_queue, sqs_dlq):
    while True:
        messages = sqs_client.receive_message(
            QueueUrl=sqs_dlq,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
            MessageAttributeNames=["All"],
        )
        if "Messages" in messages:
            for m in messages["Messages"]:
                new_MessageAttributes = {}  # Declaring empty Dictonary
                retryCount = 1  # Setting retry Counter as 1 since it is a New message.
                current_retry_count = 0
                if (
                    "MessageAttributes" in m
                ):  # Checking whether Message Attributes exists in Original Message
                    new_MessageAttributes = m["MessageAttributes"]
                    if "retryCount" in m["MessageAttributes"]:
                        retryCount = (
                            int(m["MessageAttributes"]["retryCount"]["StringValue"]) + 1
                        )
                        current_retry_count = int(
                            m["MessageAttributes"]["retryCount"]["StringValue"]
                        )

                new_MessageAttributes["retryCount"] = {
                    "StringValue": str(retryCount),
                    "DataType": "Number",
                }

                if current_retry_count <= max_retries:
                    sendAndDeleteQueue(
                        sqs_source_queue,
                        m["Body"],
                        new_MessageAttributes,
                        sqs_dlq,
                        m["ReceiptHandle"],
                    )

                else:
                    # Need to Store Message in S3 Bucket before finally deleting the message from recieve Queue
                    ct = (
                        datetime.datetime.now().timestamp()
                    )  # Calculating Current Timestamp
                    s3_key = (
                        s3_prefix_stage
                        + "/"
                        + d4
                        + "/"
                        + str(ct)
                        + "_"
                        + m["MessageId"]
                        + ".json"
                    )
                    message_data = json.dumps(
                        {"Body": m["Body"], "Attribute": new_MessageAttributes}
                    )
                    s3.put_object(Body=message_data, Bucket=s3_bucket, Key=s3_key)
                    sqs_client.delete_message(
                        QueueUrl=sqs_dlq, ReceiptHandle=m["ReceiptHandle"]
                    )
        else:
            print("Queue is currently Empty or Messages are Invisible")
            break


process_sqs_message(sqs_source_queue,sqs_dlq)
``` 
![image](https://github.com/user-attachments/assets/a5bd3757-a347-4949-8cda-ab66bfd4fb0d)
