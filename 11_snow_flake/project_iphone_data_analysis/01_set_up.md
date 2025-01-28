#### Step 1
Create data base named dw_course_db
#### Step 2
Create schema named iphone_data_analysis
#### Step 3
Create table named iphone_data
Note: While creating the table, choose the standard type.</br>
In this way, you can create table using SQL
```python
create table iphone_data (
    product_name STRING,
    product_url STRING,
    brand STRING,
    sales_price INTEGER,
    mrp INTEGER,
    discount_percentage INTEGER,
    no_of_ratings INTEGER,
    no_of_reviews INTEGER,
    upc STRING,
    star_rating FLOAT,
    ram STRING
    )
    comment = 'This table contains information about the iphone data';
```
#### Step 4
Loading the data
We can upload the data through an excel sheet 
