----------------------------------------------------------------------------------------------------------
<ins>Step 7 :</ins> Elastic Container Reposiroty(ECR) creation through AWS console</br>
Create ECR named `docker_image_of_python_libs_needed_for_lambda_ecr`

----------------------------------------------------------------------------------------------------------
<ins>Step 8 :</ins> Push image to ECR</br>
- Select the ECR named `docker_image_of_python_libs_needed_for_lambda_ecr`, which is created in above step & click `View push commands`.</br>
  You will be greated with some commands.</br>
- These commands include the commands to build docker image, authenticate to ECR, push the image to ECR etc.</br>
- Execute them one by one.

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
- Create environment variables</br>
```python
  s3_cleansed_layer = s3://trending-youtube-video-statistics-cleaned-data-heidi
```

----------------------------------------------------------------------------------------------------------
