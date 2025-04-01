1. Login `https://oaylmll-aeb33440.snowflakecomputing.com/console/login#/`
2. One of the snow flake query requires s3 bucket named `irisseta-heidi`.</br>
   So, before executing those queries, create this bucket in AWS.</br>
   Also, include AWS access key & security key in the query before executing.
   

4. For the first time, select SQL Worksheet & execute below code.
    ```python
    # Drop database if required
      drop database if exists ramu;
    # Create Database
      create database if not exists ramu;
    # use the database
      use ramu;
      create file format parquet_format TYPE=parquet;
    # stage creation
      create or replace stage ramu.PUBLIC.snow_simple url="s3://irisseta-heidi/" 
      credentials=(aws_key_id='', aws_secret_key='');
    # Check the data present in S3
      list @ramu.PUBLIC.snow_simple;
    ```
  ![image](https://github.com/user-attachments/assets/10d8bd36-827c-4871-9656-49add391ea48)

  ![image](https://github.com/user-attachments/assets/0b6bbcf0-b000-45c2-bcc0-e7c7f9f2fbcf)


4. From next time when you login. There is no need to create database. 
   Just select the existing database through
   ![image](https://github.com/user-attachments/assets/6d0bea71-2a53-40b1-97c3-6302c0a5c71c)
