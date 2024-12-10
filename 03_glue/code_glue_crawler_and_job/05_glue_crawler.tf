# Glue Data Catalog Database
resource "aws_glue_catalog_database" "crawler_output_db" {
  name = "crawler_output_db"
}

# crawler
resource "aws_glue_crawler" "glue_crawler_heidi" {
  database_name = aws_glue_catalog_database.crawler_output_db.name
  name          = "glue_crawler_heidi"
  role          = aws_iam_role.glue_service_role.name
  s3_target {
    path = "s3://${aws_s3_bucket.source_data_heidi.id}"
  }
}

# run the crawler as soon as it's created.
resource "aws_glue_trigger" "glue_crawler_heidi_run" {
  name = "glue_crawler_heidi"
  type = "ON_DEMAND"
  actions {
    crawler_name = aws_glue_crawler.glue_crawler_heidi.name
  }
}
