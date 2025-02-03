#### Suppose you have some data inside the dimension tables. How do you change it?
#### Option 1 
- New values overwrites the old value & no history of old value is maintained.
![image](https://github.com/user-attachments/assets/b9bd25d4-41e1-4f94-a42a-37e8e653d9db)

#### Option 2
- New values don't overwrite the old value.
- Whenever new value comes in, we create an new row.
- There are multilpe ways to do this, but, let's look at the way of using an `flag`.
- #### Using flag
  From below table, we can infer that:
  He was first living in New York --> Then moved to New Jersy --> Now he is in Miami
  ![image](https://github.com/user-attachments/assets/e81ffc73-dbed-4796-986a-4c4aeee8f2b1)
- #### Using version
  ![image](https://github.com/user-attachments/assets/1d8b7dc7-027a-46ec-bc4c-c384335a95f8)
- #### Using date ranges
  ![image](https://github.com/user-attachments/assets/debf98bc-4941-40ad-9985-88616867742b)

#### Option 3
- Here, will maintain partial history, not complete history.
  ![image](https://github.com/user-attachments/assets/228ed0e5-5103-42ef-9086-81a391ca6102)

#### Option 4
It's a combination of many things.
![image](https://github.com/user-attachments/assets/61319447-7000-4d1a-9b49-5340513bf6c5)
