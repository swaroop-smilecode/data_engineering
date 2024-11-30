#### What is numpy?
numpy, which stands for Numerical Python, is a library consisting of multidimensional array objects.
We can install numpy by `pip install numpy`

#### How to create arrays in Python?
Look at the below code. Here we are converting python list object into numpy array object whose name is `np`.
```python
import numpy as np

my_list = [10, 20, 30] # From list: 1d array
ndarry = np.array(my_list)
```

#### How to represent 1-d, 2-d & 3d arrays in python
Observe that 2-d array is nothing but matrix.
![image](https://github.com/user-attachments/assets/265af33e-51d1-4131-b673-26814f50a6d3)

#### Important functions of array object
#### shape
This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m).
```python
import numpy as np

my_list = [10, 20, 30]
array = np.array(my_list)
array.shape # (3,)
```
#### dtype
```python
import numpy as np

my_list = [10, 20, 30]
array = np.array(my_list)
array.dtype # dtype('int32')
```
#### reshape
```python
# Will see later.
```
#### arange
```python
import numpy as np

np.arange(0, 10, 3) # array([0, 3, 6, 9])
```
#### zeros 
```python
import numpy as np

np.zeros((2, 3)) # array([[0., 0., 0.],
                 #        [0., 0., 0.]])
```
#### ones
```python
import numpy as np

np.ones((2, 5)) # array([[1., 1., 1., 1., 1.],
                #        [1., 1., 1., 1., 1.]])
```
#### linspace
Let's understand through an example. 
question is to divide the range 1 to 10 into 7 intervals.
```python
import numpy as np

np.linspace(0, 10, 7) # array([ 0.        ,  1.66666667,  3.33333333,  5.        ,  6.66666667,
                      #         8.33333333, 10.        ])
```
#### rand
```python
import numpy as np

np.random.rand(3, 4) # array([[0.24327936, 0.0783221 , 0.7687696 , 0.47928363],
                     #        [0.7119545 , 0.60920914, 0.57668337, 0.62228376],
                     #        [0.38209233, 0.15640246, 0.57730781, 0.25935787]])
```
#### randint
```python
import numpy as np

np.random.randint(4, 40, 10) # array([21, 33, 30, 34, 22,  7,  7, 12, 33, 18])
```
#### randn
```python
import numpy as np

np.random.randn(2, 3) # array([[ 0.06832391,  0.57957572,  0.82122809],
                               [-1.5736223 ,  0.23863195, -0.05318879]])
```
