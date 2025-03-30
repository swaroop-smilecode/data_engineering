At the end of this page; there is Approach 2.</br>
That's the approach usually followed in any data processing work.

----------------------------------------------------------------------------
Let's consider a simple data processing architecture as shown below, without SQS.
![image](https://github.com/user-attachments/assets/7d5feb08-4c94-4b33-8441-7bfc1df6c704)

But the problem with this is:</br>
Let's consider data providers stored files a, b, c on 01_march_2025 in s3_bucket_input --> lambda ran --> processed data stored in Data warehouse.</br>
Next day, i.e. on 02_march_2025, let's consider they stored some more files named d, e, f in s3_bucket_input & </br>
This time when lambda runs, it will process already processed files a, b & c once again.

----------------------------------------------------------------------------
<ins>Approach 1:</ins></br>
Data providers has to send `metadata.json` file along with the data files which need to be processed.</br>
This `metadata.json` contains date & corresponding files sent on that particular date.
![image](https://github.com/user-attachments/assets/a63fb5e3-91bc-4f57-a858-e9e634d2e9ad)

----------------------------------------------------------------------------
<ins>Approach 2:</ins></br>
In this approach, data providers need not to take care of sending metadata.json file. All that they need to send is just the data files</br>
Whenever a data file lands in s3, s3 sends an message to SQS</br>
On the otherside of coin, lambda keeps polling SQS. So, lambda starts processing only those files whose information is present in the message.
![image](https://github.com/user-attachments/assets/a98ccf26-5c71-41e9-975b-8d746ee9dfd8)

----------------------------------------------------------------------------
