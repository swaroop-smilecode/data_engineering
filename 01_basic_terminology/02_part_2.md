#### -----------------------------------------------------------
#### Data Pipeline
What happens in crude oil pipeline?</br>
crude oil comes from one end --> at each stage machines process it --> At the end of the pipe, petrol comes out.
![image](https://github.com/user-attachments/assets/d92a3d13-2d9b-46fe-9d03-8e15736cd847)

data pipeline also the same. raw data comes at one end --> processed data emerges out from another end.
![image](https://github.com/user-attachments/assets/7d3efae5-770c-497a-a910-b1a09a70c97c)
#### -----------------------------------------------------------
#### Data warehouse
- It is a central repository of information that can be analyzed to make more informed decisions.</br>
  Data is copied into data warehouse from many sources such as relational databases(transactional systems),</br>
  non-relational databases(for example; dynamo db) etc.</br>
- A database is designed to store transactional data immediatly after the transaction.</br>
  where as, a data warehouse is designed for archive purpose. To put the samething in technical terms,</br>
  Data warehouse is for Online analytical processing(OLAP).</br>
  Database is for Online transactional processing(OLTP).</br>
![image](https://github.com/user-attachments/assets/4bfe912a-500b-47e8-b307-218facbe683e)
#### -----------------------------------------------------------
#### Data lake vs Data warehouse
![image](https://github.com/user-attachments/assets/97b11a24-2a58-44f6-936c-f561ba27fcda)
#### -----------------------------------------------------------
#### Extract, transform, and load (ETL) Process
![image](https://github.com/user-attachments/assets/a3e05f81-c884-4e07-8164-689a558f3326)
Just above, we saw data is collected from many sources & stored into data warehouse. This ETL process is just about that.</br>
It explains about the 3 steps involved in this process.</br>
#### <ins>Extract</ins>
Collecting data from multilpe sources & storing in temporary data warehouse(technical term is staging area).</br> 
#### <ins>Transform</ins>
1. Data Filtering</br>
   - Certain columns or rows are filtered out before saving or inserting the data into the data storage.
   - Example: For the table sales_2021, you filter out all data from orders that were placed before 2021-01-01.
2. Data Mapping</br>
   - Example: Take product names from your eCommerce shop across all language variants and translate them into English</br>
     before inserting them into the product_details table.
3. Data de-duplication</br>
   - Example: Let's consider an application(micro services architecture) in which two of the micro services deals with order of an item.</br>
     assume that one micro service uses postgresql database & another uses the dynamo db.</br>
     in this case, data related to order gets stored both in postgresql & dynamo db.</br>
     so, when you ectract data from postgresql, dynamo db and try to store it in datawarehouse(example is s3), dulpicate data is coming.</br>
     removing that duplicate data is called as data de-duplication.
4. Derived Variables</br>
   - Example: You create a column “profit” in your orders table that is computed by subtracting taxes, shipping_costs,</br>
     from your sales_total for each row (aka order).
5. Data Sorting or Ordering</br>
   - Before saving the data, you sort it by date, so it is easier to find via search.
6. Joining data from multiple sources</br>
   - Example: Join Facebook Ads spend data, Google Ads spend data and Linkedin Ads spend data into a single table called digital_advertising_spend. 
7. Aggregating data</br>
   - Example 1: Compute the total number of new customers (grouped metric) on each date (dimension).
   - Example 2: Find total sales (grouped metric) by geographical region (dimension). 
8. Splitting data</br>
   - When working with unstructured and semistructured data (such as strings, JSON, or XML files), you split the data before saving it into a table.
   - Example 1: You get the customer address in the form of the string “Boulevard avenue 23, Portobello PO1234, UK”.</br>
     Before saving it into the customer table, you split it into the columns:</br>
     street, city, zip_code, and  country.</br>
#### <ins>Load</ins>
Copy the transformed data from s3 to final destination(Example, redshift).

#### How to choose which transformation to apply?
The choice of transformation type ultimately depends on your business needs.
Get yourself on the right track by following this process:
1. Identify the target tables schema</br>
   Prepare a list of tables and their schemas (columns, possible values, etc.) of how the data would ideally look once</br>
   it has been cleaned and loaded into the target database or data warehouse.
2. Record the gap between target and incoming data</br>
   Contrast the ideal target state with the raw data you collected in the extraction step.</br>
   Note down what transformation (types) would be needed to convert the raw data into the cleaned data.‍
3. Implement the changes needed to bridge the gap between extracted data and target data</br>
   Validate the transformations before setting them on autopilot with one of the ETL tools.
#### -----------------------------------------------------------
