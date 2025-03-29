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
sqs_dlq = "<url_of_dlq>"
sqs_source_queue = "<url_of_sqs>"
s3_prefix_stage = "unprocessedmessages"
                  # folder_path_starting_from_bucket_name.
                  # Yes, just from bucket name, it's enough.
                  # Since bucket name is unique one across the wolrd,
                  # AWS knows how to find your bucket even if you just specify the bucket name>"
s3_bucket="<bucket_name>"
max_retries=
```
