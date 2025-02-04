Once you've created a stage, you can use the COPY command to load data into a table from the stage.

#### Loading data from an internal stage:
```python
COPY INTO my_table
FROM '@my_internal_stage/file.csv'
FILE_FORMAT = (TYPE = 'CSV');
```
#### Loading data from an external stage:
```python
COPY INTO my_table
FROM '@my_external_stage/file.csv'
FILE_FORMAT = (TYPE = 'CSV');
```
