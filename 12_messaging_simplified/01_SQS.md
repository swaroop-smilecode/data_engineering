##### What is SQS?
Fully managed message queuing system.

##### Architecture
`System A` : Producer</br>
`lambda` : Consumer
![image](https://github.com/user-attachments/assets/1b04c88f-8db1-4584-b2ff-03e9722f059a)

-----------------------------------------------------------------------------------------

![image](https://github.com/user-attachments/assets/30638ade-3ca5-4d35-bf92-9d27f2f41f4b)

##### How it works?
Let's consider `System A` puts some message into `SQS`</br>
SQS will not forward that message to lambda, instead lambda has to keep on polling SQS periodically.
