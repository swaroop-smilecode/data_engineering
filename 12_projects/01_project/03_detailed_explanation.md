##### <ins>Step 1: Configure AWS CLI</ins>
- It's a package of commands.
- Once installed, they are available to be executed through CLI.</br>
- By executing those commands, you can do everything that are done through AWS portal, usuallay.
- Think: behind the scenes, those commands are opening AWS portal & doing work.</br>
  Hence, they need to know your AWS ID & Password.</br>
  In order to tell to AWS commands about ID & Password, corresponding commands is `aws configure`.
  ```python
  aws configure
  AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
  AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  Default region name [None]: us-west-2
  Default output format [None]: json
  ```

##### <ins>Step 2: Create below s3 buckets</ins>
```python
input-data-heidi # To store the input data that needs to be analyzed
output-data-heidi # To store the output data that is analyzed 
```

##### <ins>Step 3: Load input data which needs to be analyzed into data lake(s3)</ins>
- The data which needs to be analyzed is present on cloud & it can be accessed by hitting API `https://cdn.wsform.com/wp-content/uploads/2020/06/industry_sic.csv`</br>
- Hit the API to download data & then upload it into s3 bucket through below steps.</br>
  ```python
  curl -o industry_sic.csv "https://cdn.wsform.com/wp-content/uploads/2020/06/industry_sic.csv"
  aws s3 cp industry_sic.csv s3://input-data-heidi/industry_sic.csv
  ```
- <ins>Note:</ins></br>
  If you need sample csv files for project need, below is good website</br>
  https://wsform.com/knowledgebase/sample-csv-files/

##### <ins>Step 3: pyspark code</ins> 
```python
import sys
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *

# spark session creation 
spark = SparkSession \
        .builder \
        .appName("airflow_with_emr") \
        .getOrCreate()

def main():
    s3_location = "s3://input-data-heidi/";
    industry_sic_df = spark.read.format("csv").option("inferSchema","true").load(s3_location);
    analyzed_df = industry_sic_df.groupBy("SIC Code").count()
    analyzed_df.coalesce(1).write.format("parquet").mode('overwrite').save("s3://output-data-heidi/industry_sic.csv")

main()
```
