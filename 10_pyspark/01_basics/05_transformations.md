#### What is transformation?
- Changing the data inside an data frame is called as transformation.
- Dataframes are immutable.
- Transformations are the core of how you express your business logic using Spark.
#### Types of transformations:
1. Narrow dependency transformations.
2. Wide dependency transformations.

<ins>1. Narrow dependency transformations</ins></br>
One input partition will contribute to only one output partition.
![image](https://github.com/user-attachments/assets/e1ad0f3f-bd11-45cb-8525-cccc2ad0896f)

<ins>2. Wide dependency transformations</ins></br>
One input partition will contribute to only n output partition's.
![image](https://github.com/user-attachments/assets/cf5976e3-8283-478e-94dc-a7af2c12f7bf)
