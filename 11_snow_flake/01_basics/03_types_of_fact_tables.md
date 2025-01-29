#### What is fact table?
A fact table is a table in a star schema or snowflake schema of a data warehouse that stores numerical data for analysis.</br>
These tables typically contain foreign keys pointing to dimension tables.

#### Transaction fact tables
The transaction fact table records individual transactions at the most atomic level of detail.</br>
Each row transactional fact table represents a single event, such as a sales transaction or an order fulfillment event,</br>
making these fact tables ideal for detailed analysis of daily business activities.
![image](https://github.com/user-attachments/assets/669dc2c9-7978-41d3-b093-cf32702010e8)

#### Periodic snapshot tables
- A full periodic snapshot table or fact table summarizes business activities over a defined period, such as daily, weekly, or monthly.</br>
  Unlike transaction fact tables, periodic snapshot tables do not store individual transactions but provide a performance summary at regular intervals.
- Ideal for trend analysis over time (e.g., daily sales volume or inventory levels at the end of each day).

#### Accumulating Snapshot Tables
- An accumulating snapshot fact table tracks the progress of events that have a defined life cycle, such as the order fulfillment process.</br>
  These periodic snapshot fact tables capture the evolving state of a process from start to finish by updating rows as the process advances through its stages.
- The same row is updated multiple times as the process progresses. For ex: Accumulative snapshot tables capture business processes such as order processing,
  where each row represents an order moving through stages like "order received", "order shipped", and "order completed".

#### Factless Fact Table
A factless fact table contains only foreign keys from related dimension tables and no numerical or quantitative measures.

#### Aggregate Fact Table
An aggregate fact table stores summarized or aggregated data to enhance query performance.</br>
These snapshot fact tables are created by summarizing large datasets to improve the speed of reporting and analysis.
