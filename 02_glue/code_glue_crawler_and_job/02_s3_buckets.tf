# --------------------------------------------
# Source bucket creation & uploading data
resource "aws_s3_bucket" "source_data_heidi" {
  bucket        = "source-data-heidi"
  force_destroy = true
  tags = {
    Name = "source_data_heidi"
  }
}

resource "aws_s3_bucket_object" "uploading_input_csv" {
  bucket = aws_s3_bucket.source_data_heidi.id
  key    = "customer_orders.csv"
  source = "./data/customer_orders.csv"
}
# -----------------------------------------------
# Destination bucket to store the processed data.
resource "aws_s3_bucket" "destination_data_heidi" {
  bucket        = "destination-data-heidi"
  force_destroy = true
  tags = {
    Name = "destination_data_heidi"
  }
}
# -----------------------------------------------
# S3 Bucket for pyspark script
resource "aws_s3_bucket" "pyspark_script_heidi" {
  bucket        = "pyspark-script-heidi"
  force_destroy = true
}

resource "aws_s3_bucket_object" "file_03" {
  bucket = aws_s3_bucket.pyspark_script_heidi.id
  key    = "pyspark_data_transform_code.py"
  source = "./script/pyspark_data_transform_code.py"
}
# -----------------------------------------------
