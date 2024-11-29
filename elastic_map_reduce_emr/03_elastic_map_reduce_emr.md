#### What is elastic map reduce?
AWS's way of map reduce framework is elastic map reduce(emr).

#### EMR architecture
![image](https://github.com/user-attachments/assets/3821872f-29fb-4f3b-8fbb-6a5a12ca97da)
<ins>Primary node:</ins></br>
A node that manages the cluster through YARN resource manager.</br>

<ins>Core nodes:</ins></br>
- Input data is distributed to core nodes & each core node will work on part of data that it receive</br>
  & sends result back to primary node.</br>
- Core nodes will read data from HDFS(Hadoop Distributed File System) type of storage system.</br>

<ins>Task nodes:</ins></br> 
They do not have any HDFS storage associated with them. They are to increase computational power.

#### Master & slave nodes can be created by using any of your choice from below services.
1. EC2
2. EKS
3. lambda

