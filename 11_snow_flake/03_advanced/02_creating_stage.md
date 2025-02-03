-----------------------------------------------
#### Creating internal stage:
```python
CREATE STAGE my_internal_stage;
```
-----------------------------------------------
#### Creating external stage:</br>
This creates an external stage named my_external_stage that points to an S3 bucket.</br>
The CREDENTIALS parameter specifies the AWS access key and secret access key needed to access the bucket.
```python
CREATE STAGE my_external_stage
  URL='s3://my-bucket/my-prefix'
  CREDENTIALS=(AWS_KEY_ID='<aws-key-id>' AWS_SECRET_KEY='<aws-secret-key>');
```
-----------------------------------------------
