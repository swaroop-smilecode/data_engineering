#### What are partitions?
To allow every executor to perform work in parallel, Spark breaks up the data into chunks called partitions.
#### Executors & partitions, both are important
In order to leverage the advantage of spark, both executors & partitions are important. Things don't work out with any one.</br>
- If you have one partition, Spark will have a parallelism of only one, even if you have thousands of executors.</br>
- If you have many partitions but only one executor, Spark will still have a parallelism of only one because there is only one computation resource.</br>
- You don't need (for most of the part) to deal with partitions manually. But, in case you want to do, spark provides the API :)
