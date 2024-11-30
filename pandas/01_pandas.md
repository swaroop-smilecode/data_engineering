#### Pandas
![image](https://github.com/user-attachments/assets/a526d014-b50a-4584-a646-1a9a218107c9)

#### Data structures in pandas
In data engineering, will be mostly using DataFrame / Series, but not Panel & Panel4D.
1. Series</br>
   One dimentional 
3. DataFrame</br>
   Two dimentional
5. Panel</br>
   Three dimentional
7. Panel4D</br>
   Four dimentional

#### Series
- Very similar to a numpy array.
- What differentiates the NumPy array from a Series, is that a Series can have index labels,</br>
  meaning it can also be indexed by a label, instead of just a number location.
  
```python
import pandas as pd

my_list = [10, 20, 30]
series = pd.Series(my_list)

series # 0    10
       # 1    20
       # 2    30
       # dtype: int64
```

```python
import pandas as pd

my_list = [10, 20, 30]
series = pd.Series(my_list)

series.index  # RangeIndex(start=0, stop=3, step=1)
```

```python
import pandas as pd

my_list = [10, 20, 30]
series = pd.Series(my_list)

series.values # [10 20 30]
```
