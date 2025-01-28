#### What is dimentional modelling?
- The method of organizing the data inside an data warehouse is called as dimentional modelling.

- There are 2 type of tables in dimentional modelling.
  1. fact table
  2. dimention table

- To get insight on data, we need both fact & also dimension.</br>
  For example; fact is profit & dimention is the year(20$ profit in the year 2024)</br>

- Usually, will have one fact table & multilpe dimention tables.</br>
  & star schema is the respective technical word.
  ![image](https://github.com/user-attachments/assets/2310efd5-0af2-4352-9784-33dfd143cddd)

- <ins>Thumb rule to recognize which data should go into fact table & which data should go into dimension table.</ins></br>
  The data that changes frequently should be part of fact table. For example, `profit`(profit changes based on time period)</br>
  The data that doesn't change frequently should go into dimention table. For example,`year`.







