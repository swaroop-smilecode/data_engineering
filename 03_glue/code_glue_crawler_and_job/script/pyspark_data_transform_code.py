# ------------------------------------------
# Bioler plate code
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
# ------------------------------------------
# Read data in CSV From AWS S3
source_dynamic_frame = glueContext.create_dynamic_frame_from_options(
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://source-data-heidi"]},
    format_options={"withHeader": True, "separator": ","},
)
# ------------------------------------------
# Write data in CSV into AWS S3
source_dynamic_frame = glueContext.write_dynamic_frame.from_options(
    frame=source_dynamic_frame,
    connection_type="s3",
    connection_options={"path": "s3://destination-data-heidi"},
    format="csv",
    format_options={
        "quoteChar": -1,
    },
)
# ------------------------------------------
