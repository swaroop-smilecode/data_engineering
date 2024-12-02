![image](https://github.com/user-attachments/assets/127b7668-835a-4efc-b99a-a763e56c85e1)

<ins>Step 1</ins>
- Create lambda named `03_lambda_spotify_data_pipeline_extract` & the corresponding code file is present in this project folder.
- The duty of this lambda function is to consume spotify API(extracting data) &</br>
  store that data as `.json` file inside bucket location `spotify-data-pipeline-heidi/raw_data/to_processed`.</br>
- So, first thing needs to be done is registering for spotify API in their developer portal,</br>
  upon which, will receive `client_id` & `client_secret`. Set them as environment variables inside lambda.</br>
- Increase lambda timeout to 1 minute.
- Create EventBridge trigger with corresponding rule as `rate(1 minute)`.</br>
  This trigger time will be as per business needs, when working in a project.</br>
  But, for learning purpose, i am setting it to 1 minute.
- To the role assigned to lambda, give permissions about the services named `cloud_watch logs`, `s3` & `lambda`.
- Create spotipy `layer` using below command.</br>
  Since lambda runs on linux os. pip installation has to be done according to linux platform.</br>
```python
mkdir python

pip install --platform manylinux2014_x86_64 --target=python --implementation cp --python-version 3.13 --only-binary=:all: --upgrade spotipy -t "C:/Users/swaro/Desktop/python"
  ```
<ins>Step 2</ins></br>
- Create lambda named `04_lambda_spotify_data_pipeline_transform` & the corresponding code file is present in this project folder.
- We know that  the lambda function present in step 1, puts `.json` file in bucket location</br>
  `spotify-data-pipeline-heidi/raw_data/to_process`.</br>
  This lambda function should get triggered whenever that `.json` file is put into bucket location</br>
  `spotify-data-pipeline-heidi/raw_data/to_process`.
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
<ins>Step 3</ins></br>
<ins>Step 4</ins></br>
<ins>Step 5</ins></br>
