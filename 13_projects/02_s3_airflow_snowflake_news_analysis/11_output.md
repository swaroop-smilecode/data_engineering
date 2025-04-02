Once the DAG ran, how to see / work on output data?
```python
-- Check the data present in s3 / not
list @ramu.PUBLIC.snow_simple;

-- Selecting whole table
SELECT * FROM ramu.PUBLIC.helloparquet;

-- Data analytics query
SELECT distinct "newsTitle", "url_source" 
FROM ramu.PUBLIC.helloparquet;
```
