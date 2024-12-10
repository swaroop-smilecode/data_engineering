# --------------------------------------------
# Source bucket creation & uploading data
resource "aws_s3_bucket" "source_data_heidi" {
  bucket        = "source-data-heidi"
  force_destroy = true
  tags = {
    Name = "source_data_heidi"
  }
}

resource "aws_s3_bucket_object" "file_01" {
  bucket = aws_s3_bucket.source_data_heidi.id
  key    = "customers.csv"
  source = "./data/customers.csv"
}

resource "aws_s3_bucket_object" "file_02" {
  bucket = aws_s3_bucket.source_data_heidi.id
  key    = "sales.csv"
  source = "./data/sales.csv"
}
# --------------------------------------------
