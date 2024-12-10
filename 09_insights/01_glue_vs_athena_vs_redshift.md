#### <ins>Athena vs Redshift</ins>
- Athena can't run SQL queries on the data that is present inside the warehouse(For ex: Redshift).</br>
  Athena works only on the data present inside S3 bucket.

#### <ins>Athena vs Glue</ins>
- Catalog can be created by athena service / glue service.
- Recommended way to generate catalog is by glue. The reason is simple. Athena can prepare catalog only based on the data from s3.</br>
  How about preparing the catalog from may sources like S3, SQL DB, No-SQL DB etc ? Only glue can do that.
   
