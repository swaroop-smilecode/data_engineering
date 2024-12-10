#### Columnar database
- Dataware houses are columner databases. The reason is, unlike the OLTP databases, during OLAP, will query only respective columns</br>
  which are interested by business & there is no need of entire row.
  ![image](https://github.com/user-attachments/assets/500f927a-45e9-422a-994d-b5a1d3be131f)

#### Why dataware houses have columnar database?
1. Faster reading spead.</br>
   For example, look at the above table.</br>
   Let's consider business requirement is to know all the employee names.</br>
   In case of row based database, query needs to reed 3 storage blocks.</br>
   In case of columnar based database, query needs to reed just 1 storage block.</br>
2. Better compression rate.</br>
   For example, look at the above table.</br> 
   In columnar database, complete block contains string type of date. So, you can choose a compression technique</br>
   which compresses string's better.</br>
   For other storage block where numeric types are stored, you can select the best compression technique suitable for numeric types.</br>
   This is not possible in case of row based database.
