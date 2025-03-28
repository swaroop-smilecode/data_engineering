---------------------------------------------------------------------------------------------------------
![image](https://github.com/user-attachments/assets/cad126c4-8ee5-483d-9b29-966f65fc0577)

#### Delay seconds
It's the amount of time to delay the visibility of incoming message.

#### Visibility timeout
- The amount of time to make the message invisible after it has been read by a consumer.
- What's the need?
  When one consumer is consuming a message, the same message should not be consumed by others.</br>
  Why?</br>
  Why do you want same message to be processed by multilpe AWS services? That's not the purpose of SQS</br>

---------------------------------------------------------------------------------------------------------
#### Dead letter queue
The AWS services should try only for a limited number of times to work on a particular message.</br>
It's not advisable to keep working on same message even if the corresponding work can't be done due to some reason. Why?</br>
There are other messages coming into queue. Why not work on them, instead of working on something whose work can't be completed?

---------------------------------------------------------------------------------------------------------
