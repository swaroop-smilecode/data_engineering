# -------------------------------------------------------------------------------------
# Create lambda
# Choose one of the following options to create your function : `Container image`
# Function name : `input_data_json_to_parquet_lambda`
# Container image URI : 
# -------------------------------------------------------------------------------------
# By default, an IAM role with basic permissions will be created & attached to lambda.
# Add more permissions to it according to your need.
# For POC purpose, just add AdministratorAccess policy to the role, so that you won't face any permission related problems.
# -------------------------------------------------------------------------------------
# Increase the maximum execution time of lambda to 1 minute
# -------------------------------------------------------------------------------------
# Create s3 bucket named trending-youtube-video-statistics-cleaned-data-heidi
# Will stored cleaned data here
# -------------------------------------------------------------------------------------
# Create 4 environment variables
# s3_cleansed_layer = trending-youtube-video-statistics-cleaned-data-heidi
# glue_catalog_db_name = trending_youtube_videos_analysis_database
# glue_catalog_table_name = raw_statistics_reference_data
# write_data_operation = append
# -------------------------------------------------------------------------------------
import pyarrow
import pandas as pd
import urllib.parse
import os

os_input_s3_cleansed_layer = os.environ["s3_cleansed_layer"]
os_input_glue_catalog_db_name = os.environ["glue_catalog_db_name"]
os_input_glue_catalog_table_name = os.environ["glue_catalog_table_name"]
os_input_write_data_operation = os.environ["write_data_operation"]


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )
    try:

        # Creating DF from content
        df_raw = wr.s3.read_json("s3://{}/{}".format(bucket, key))

        # Extract required columns:
        df_step_1 = pd.json_normalize(df_raw["items"])

        df.to_parquet("myfile.parquet", engine="fastparquet")
        # Write to S3
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation,
        )

        return wr_response
    except Exception as e:
        print(e)
        print(
            "Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.".format(
                key, bucket
            )
        )
        raise e
