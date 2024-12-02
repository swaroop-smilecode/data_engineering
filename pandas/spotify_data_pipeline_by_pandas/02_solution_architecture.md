--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### Architecture
![image](https://github.com/user-attachments/assets/5d7aca78-c5c7-4d63-8166-997d94039fe9)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### <ins>Step 1(Data extraction)</ins>
- Create lambda named `03_lambda_spotify_data_pipeline_extract` & the corresponding code file is present in this project folder.
- The duty of this lambda function is to consume spotify API(extracting data) &</br>
  store that data as `.json` file inside bucket location `spotify-data-pipeline-heidi/raw_data/to_processed`.</br>
- So, first thing needs to be done is registering for spotify API in their developer portal,</br>
  upon which, will receive `client_id` & `client_secret`. Set them as environment variables inside lambda.</br>
- Increase lambda timeout to 1 minute.
- Create EventBridge trigger with corresponding rule as `rate(1 minute)`.</br>
  This trigger time will be as per business needs, when working in a project.</br>
  But, for learning purpose, i am setting it to 1 minute.
  ![image](https://github.com/user-attachments/assets/78bd0d1f-2bb5-4399-846e-1d10395460c5)
- To the role assigned to lambda, give permissions about the services named `cloud_watch logs`, `s3` & `lambda`.
- Create spotipy `layer` using below command.</br>
  Since lambda runs on linux os. pip installation has to be done according to linux platform.</br>
```python
mkdir python

pip install --platform manylinux2014_x86_64 --target=python --implementation cp --python-version 3.13 --only-binary=:all: --upgrade spotipy -t "C:/Users/swaro/Desktop/python"
  ```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### <ins>Step 2(Data Transformation)</ins></br>
- Create lambda named `04_lambda_spotify_data_pipeline_transform` & the corresponding code file is present in this project folder.
- We know that  the lambda function present in step 1, puts `.json` file in bucket location</br>
  `spotify-data-pipeline-heidi/raw_data/to_process`.</br>
  This lambda function should get triggered whenever that `.json` file is put into bucket location</br>
  `spotify-data-pipeline-heidi/raw_data/to_process`.
  So, create an trigger for that as shown below.
  ![image](https://github.com/user-attachments/assets/1df651d9-752b-4a16-a652-b53041206fa5)
- The duty of this lambda function is:</br>
  1. Consume data present in `.json` file & create data frames out of that data.</br>
     (Because pandas can tranform data which is present in the form of dataframe.)</br>
  2. Transform data frames as per business needs.</br>
  3. Create .csv file from transformed data frames & sotre it in bucket named `spotify-data-pipeline-heidi/transformed`.</br>
- Increase lambda timeout to 1 minute.
- To the role assigned to lambda, give permissions related to cloud_watch logs, s3 & lambda.
- Create pandas `layer` using below command.</br>
  Since lambda runs on linux os. pip installation has to be done according to linux platform.</br>
```python
mkdir python

pip install --platform manylinux2014_x86_64 --target=python --implementation cp --python-version 3.13 --only-binary=:all: --upgrade spotipy -t "C:/Users/swaro/Desktop/python"
  ```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### <ins>Step 3(Data Loading)</ins></br>
- Inside AWS glue service, there is a functionality named glue crawler.</br>
  You may not see the need of this crawler when reading data from single source like spotify api,</br>
  but, suppose you want to execute an SQL query at a time on multiple data sources like</br>
  spitify api, postgresql(sql) database, dynamo db(no-sql) database, how would you do that?</br>
  That's where crawler comes into picture. It creates schema about the data present in different sources at single location,</br>
  so that you can run your query on that schema & behind the scenes,</br>
  crawler will go to different sources to fetch data & you no need to worry :)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
