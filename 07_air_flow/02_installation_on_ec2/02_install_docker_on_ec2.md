------------------------------------------------------------------------------------------------------------------------------
Create EC2 instance with below settings</br>
- Name
  ```python
  default_ec2
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
  ```python
  True
  ```
- Security group
  ```python
  default
  ```
- Configure storage
  ```python
  32 GB hard disk
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
