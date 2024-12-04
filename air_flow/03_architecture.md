#### Architecture:
![image](https://github.com/user-attachments/assets/f03b6892-fee9-431c-a26f-28be1bdf0e38)

![image](https://github.com/user-attachments/assets/57ff94c2-2584-4f87-9e56-4c44312a3ac8)

#### Typs of executors:
------------------------------------------------------------------------------------------------------------------------------
<ins>Local executors:</ins></br>
Sequential executor</br>
- Default executor(You don't have to configure any thing in air flow to do your work).
- The name itself says sequential. So, no parallel running of tasks. One task at a time.
- It's not cluster. Hence, no high availability & scalability. Therefore not suitable for production.

Local executor</br>
- Similar to sequential executor, with only one difference. Tasks can be executed in parallel.
- Just a parameter needs to be set in the config file to select local executor. That's it, no more additional setup.
------------------------------------------------------------------------------------------------------------------------------
<ins>Remote executors</ins></br>
Celery executor</br>
![image](https://github.com/user-attachments/assets/fdea7bf7-0d28-40bb-bfd4-35268e4599e5)

Kubernetes executor</br>
![image](https://github.com/user-attachments/assets/2acd84f5-ba9f-4b20-8000-06cc86cb95ce)

------------------------------------------------------------------------------------------------------------------------------
