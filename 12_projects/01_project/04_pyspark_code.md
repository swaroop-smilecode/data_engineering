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
