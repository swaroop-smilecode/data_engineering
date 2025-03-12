------------------------------------------------------------------------------------------------------------------------------
Create EC2 instance with below settings</br>
- Name
  ```python
  airflow_on_docker
  ```
- Instance type
  ```python
  t2.large
  ```
- Key pair
  ```python
  default_key_pair
  ```
- VPC
  ```python
  default_vpc-vpc
  ```
- Subnet
  ```python
  default_vpc-subnet-public3-us-east-1c
  ```
- Auto-assign public IP
  (If you don't set to True, you can't connect through `connect` button on AWS)
  ```python
  True
  ```
- Security group
  ```python
  default
  ```
- Configure storage
  ```python
  96 GB hard disk
  ```

------------------------------------------------------------------------------------------------------------------------------
Connect to it using `EC2 instance connect`(AWS portal).</br>

------------------------------------------------------------------------------------------------------------------------------
Install docker</br>
```python
sudo su
yum install docker
```

------------------------------------------------------------------------------------------------------------------------------
