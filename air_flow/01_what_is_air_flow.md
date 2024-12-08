#### Cron job
Before understanding what is air flow. It's absolutely necessary to understand `cron` command in linux OS.</br>
We know servers are hosted on linux OS. 
For example, consider an database server hosted on linux OS.</br>
To achieve high availability, backup needs to be taken periodically.</br>
This task/job can be achieved by cron command.</br>

For more info, refer below.</br>
https://www.splunk.com/en_us/blog/learn/cron-jobs.html</br>
https://www.hostinger.in/tutorials/cron-job

#### Air flow
Let's consider, there are 100's of cron job's in your application.</br>
All these jobs to be monitored for failed/passed status --> If failed, send alerts to email & execute it again.</br>
Imagine the amount of work that needs to be done here 😲</br>

On top of that, as the business grows, cron jobs architecture becomes like this
![image](https://github.com/user-attachments/assets/e3681683-effd-4263-941e-220da0053ae9)

This is where air flow comes in. It's an orchestrator of cron jobs. 
![image](https://github.com/user-attachments/assets/407fa6a7-95ca-422d-b401-652f41c0cadb)

#### Let's put it in simple terms.
All the above thing is going in depth. To look on top in simple terms, airflow is just below.
![image](https://github.com/user-attachments/assets/7b508329-7d2e-4ce3-be28-ef6f663839b7)

![image](https://github.com/user-attachments/assets/f72bd2b8-956d-44eb-9873-f911b0a017ef)

![image](https://github.com/user-attachments/assets/c51a6ee0-3231-495c-b121-6e97136a07b5)
