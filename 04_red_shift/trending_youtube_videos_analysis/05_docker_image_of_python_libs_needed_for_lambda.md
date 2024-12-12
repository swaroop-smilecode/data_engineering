----------------------------------------------------------------------------------------------------------
#### What's the reason for using docker container which will be triggered by lambda, instead of directly coding in lambda?
Our code used to clean data needs below libraries.
```python
awswrangler
pandas
```
For a lambda function, there can be maximum of 5 layers &</br>
total size of libraries provided in those 5 layers should not exceed 250 MB when you unzip them.</br>

That's the reason to go with docker container which will be triggered by lambda.

----------------------------------------------------------------------------------------------------------
<ins>Step 1 :</ins> Docker installation & starting the service</br>
To create docker image we need docker installed. That's what we are going to do now.</br>
- Create an EC2 instance named `docker_trending_youtube_videos_analysis`(free tier is good enough).
- Once the image is created, we want to push that image to `ECR` which is an aws service.</br>
  To do that, you(`you means, the user showed in command promt of EC2 machine`) need to have access to ECR.</br>
  For this purpose, let's configure aws credentials.</br>
  For configuring credentials, you need `awscli` & it comes by default with EC2 instance.</br>
  So, you no need to install it, just start using the awscli commands.
  ```python
  aws configure
  AWS Access Key ID [None]: <Keep your access key id here>
  AWS Secret Access Key [None]: <Keep your access key here>
  Default region name [None]: us-east-1
  Default output format [None]: press enter
  ```
- Install & start docker server.
  ```python
  sudo su
  yum install -y docker
  service docker start
  ```
----------------------------------------------------------------------------------------------------------
<ins>Step 2 :</ins> Project folder creation</br>
Create project folder & navigate into it.
  ```python
  mkdir docker_image_creation
  cd docker_image_creation
  ```
----------------------------------------------------------------------------------------------------------
<ins>Step 3 :</ins> lambda_function.py</br>
  ```python
  nano lambda_function.py
  ```
Paste below content inside the file & save it.</br>
Observe that the fn name is `handler` not `lambda_handler`.
  ```python
import awswrangler as wr
import pandas as pd
import urllib.parse
import os

os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']


def handler(event, context):
    # Get the object from the event and show its content type
    bucket = "trending-youtube-video-statistics-raw-data-heidi"
    key = "raw_statistics_reference_data/CA_category_id.json"
    try:

        # Creating DF from content
        df_raw = wr.s3.read_json('s3://{}/{}'.format(bucket, key))

        # Extract required columns:
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write to S3
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )

        return wr_response
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
  ```
----------------------------------------------------------------------------------------------------------
<ins>Step 4 :</ins> Creating lambda fn `input_data_json_to_parquet_lambda` through AWS console</br>
While creating lambda, these are the choices you need to take</br>
- Choose one of the following options to create your function : `Container image`</br>
  Function name : `input_data_json_to_parquet_lambda`</br>
  Container image URI :
- By default, an IAM role with basic permissions will be created & attached to lambda.</br>
  Add more permissions to it according to your need.</br>
  For POC purpose, just add AdministratorAccess policy to the role, so that you won't face any permission related problems.
- Increase maximum execution time of lambda to 1 minute
- Create 4 environment variables</br>
```python
  glue_catalog_db_name = trending_youtube_videos_analysis_database
  glue_catalog_table_name = raw_statistics_reference_data/CA_category_id.json
  s3_cleansed_layer = s3://trending-youtube-video-statistics-cleaned-data-heidi
  write_data_operation = append
```
----------------------------------------------------------------------------------------------------------
<ins>Step 5 :</ins> requirements.txt</br>
```python
nano requirements.txt
```
Paste below content inside the file.
```python
awswrangler
pandas
```
Press below keys
```python
ctrl + x
y
Enter
```
----------------------------------------------------------------------------------------------------------
<ins>Step 6 :</ins> Dockerfile</br>
```python
nano Dockerfile
```
Paste below content inside the file & save
```python
FROM public.ecr.aws/lambda/python:3.12

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]
```
----------------------------------------------------------------------------------------------------------
<ins>Step 7 :</ins> Elastic Container Reposiroty(ECR) creation through AWS console</br>
Create ECR named `docker_image_of_python_libs_needed_for_lambda_ecr`

----------------------------------------------------------------------------------------------------------
<ins>Step 8 :</ins> Push image to ECR</br>
- Select the ECR named `docker_image_of_python_libs_needed_for_lambda_ecr`, which is created in above step & click `View push commands`.</br>
  You will be greated with some commands.</br>
- These commands include the commands to build docker image, authenticate to ECR, push the image to ECR etc.</br>
- Execute them one by one.
