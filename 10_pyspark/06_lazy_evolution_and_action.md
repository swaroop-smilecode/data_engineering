#### Lazy evolution & Action
- When you run below program, spark will not execute the code step by step. Instead, when it sees `action`,</br>
  it prepares the best execution plan & then executes it.
  ```python
  data_frame.do_a() # Transformtion 1
  data_frame.do_b() # Transformtion 2
  data_frame.do_c() # Transformtion 3
  action # Now, spark prepares execution plan & then executes it.
  ```
- By waiting until the last minute to execute the code, Spark compiles this plan from your raw DataFrame transformations</br>
  to a streamlined physical plan that will run as efficiently as possible across the cluster.</br>
- <ins>Types of action:</ins></br>
  There are three kinds of actions
  1. Actions to view data in console
  2. Actions to collect data to native objects in the respective language
  3. Actions to write to output data sources
