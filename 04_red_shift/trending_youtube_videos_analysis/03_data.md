#### Dumping data into data lake(S3)
- Create s3 bucket named `trending-youtube-video-statistics-raw-data-heidi`.
- While creating bucket, uncheck `Block all public access`.
- Download the data from `https://www.kaggle.com/datasets/datasnaek/youtube-new` into your project folder(Let's keep the data in `data` folder).</br>
- Upload the data from data folder to s3 bucket folder `raw_statistics_reference_data/`.</br>
  Observe that the folder is also going to be created by below command. You no need to create folder, before execution of the command.</br> 
  ```python
  aws s3 cp ../data s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics_reference_data/ --recursive --exclude "*" --include "*.json"
  ```
- Upload the data from data folder to s3 bucket folder `raw_statistics/region=ca/`.</br>
  Observe that the folders are also going to be created by below command. You no need to create folders, before execution of the command.</br> 
  ```python
  aws s3 cp ../data/CAvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=ca/
  ```
  Similarly upload remaining regions data.
  You can execute all the below commands at a time. Just copy the code present inside below python block & paste it in cmd, press enter.</br>
  ```python
  aws s3 cp ../data/DEvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=de/
  aws s3 cp ../data/FRvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=fr/
  aws s3 cp ../data/GBvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=gb/
  aws s3 cp ../data/INvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=in/
  aws s3 cp ../data/JPvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=jp/
  aws s3 cp ../data/KRvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=kr/
  aws s3 cp ../data/MXvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=mx/
  aws s3 cp ../data/RUvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=ru/
  aws s3 cp ../data/USvideos.csv s3://trending-youtube-video-statistics-raw-data-heidi/raw_statistics/region=us/
  ```
#### Cleaned data
Create s3 bucket named `trending-youtube-video-statistics-cleaned-data-heidi`
Will stored cleaned data here
