![image](https://github.com/user-attachments/assets/a1d677cb-ba3a-4aff-8295-1d4f8c5b4be3)

#### Distribution styles
There are 4 distribution styles & redshift will ask you to choose from these.
1. Key
2. All
3. Even
4. Auto

<ins>Key distribution style</ins></br>
Look at the above table. Suppose you opted for key distribution style & the key you chose is ename.</br>
Then the values of this key column will go through an hashing algorithm which decides into which slice the</br>
value should go into.</br>
<ins>All distribution style</ins></br>
Look at the picture & it's self understandable.</br>
<ins>Even distribution style</ins></br>
The data will be distributed in round robin manner. Because of this, the data get's distributed evenly between slices,</br>
hence the name.</br>
<ins>Auto distribution style</ins></br>
Let redshift decide the distribution style.

#### Why distribution styles are important?
Based on type of data the table is holding, you have to choose correct distribution algorithm.</br>
Else it will result in data skewness.</br> 

#### How to define distribution styles?
When you are creating the table, distribution style of that table needs to be mentioned.</br>
After that, when each row is inserted into the table, the values will go into the respective columns</br>
decided by distribution style of the table.</br>
![image](https://github.com/user-attachments/assets/4ddc63b3-ced0-43c2-bca9-857b4248fbe1)
