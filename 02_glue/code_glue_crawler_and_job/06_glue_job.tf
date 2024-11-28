resource "aws_glue_job" "job_pyspark_data_transform_code" {
  glue_version      = "4.0"                                                                       #optional
  max_retries       = 0                                                                           #optional
  name              = "job_pyspark_data_transform_code"                                           #required
  description       = "test the deployment of an aws glue job to aws glue service with terraform" #description
  role_arn          = aws_iam_role.glue_service_role.arn                                          #required
  number_of_workers = 2                                                                           #optional, defaults to 5 if not set
  worker_type       = "G.1X"                                                                      #optional
  timeout           = "60"                                                                        #optional
  execution_class   = "FLEX"                                                                      #optional
  tags = {
    project = "read_data_from_csv_using_glue_job" #optional
  }
  command {
    name            = "glueetl"                                                                      #optional
    script_location = "s3://${aws_s3_bucket.pyspark_script_heidi.id}/pyspark_data_transform_code.py" #required
  }
  default_arguments = {
    "--enable-continuous-cloudwatch-log" = "true"
    "--class"                            = "GlueApp"
    "--enable-job-insights"              = "true"
    "--enable-auto-scaling"              = "false"
    "--enable-glue-datacatalog"          = "true"
    "--job-language"                     = "python"
    "--job-bookmark-option"              = "job-bookmark-disable"
    "--datalake-formats"                 = "iceberg"
    "--conf"                             = "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions  --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog  --conf spark.sql.catalog.glue_catalog.warehouse=s3://tnt-erp-sql/ --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog  --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO"

  }
}
