- Name: `airflow_server`
-
![image](https://github.com/user-attachments/assets/9c5700bf-3557-4e20-88de-189ab3168e23)

- Instance type: `t2.small`
- Key pair (login): `default_key_pair`
- Leave remaining as default & launch the instance.
- VPC: `default_vpc-vpc`
- Subnet: `default_vpc-subnet-public3-us-east-1c`</br>
          Observe that the subnet is public. It means, you are creating EC2 insatnce inside this public subnet,</br>
          so that requests from outside of this VPC can hit this EC2.
- Auto-assign public IP: `Enable`
- Security group: `defaultsg-06c1df0000a2a7dfa`</br>
  Type: `All traffic`(You are allowing all types of requests such as HTTP, HTTPS etc.)</br>
  Port range: `All`(You are allowing requests to all ports of this EC2 instance)
  ![image](https://github.com/user-attachments/assets/697f2e85-d126-4ea2-94bd-2c26fd42a58e)
- `Launch :)`
