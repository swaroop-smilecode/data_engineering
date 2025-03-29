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
#### Messages in flight
Let's consider that an consumer has polled for the message from SQS</br>
Then SQS thinks that the consumer is processing the message, hence it is saying `Messages available = 0` & `Messages in flight = 1`</br>
If the message got processed successfully, it's the duty of consumer to delete that messages from SQS</br>
![image](https://github.com/user-attachments/assets/b3ddecef-4ffe-4196-b460-0e8e479618e8)

SQS will keep checking, whether the message got deleted from queue / not after the `Visibility timeout`</br>
If available, then the screen looks like this:
![image](https://github.com/user-attachments/assets/f6105443-fa80-43d8-83f9-743b09d29a95)

#### ReceiptHandle
For each message that is stored inside of SQS, an attribute named `ReceiptHandle` is added to that message to uniquely identify the message.</br>
That's the attribute, based on which consumer can delete the message from queue, if it processed succesfully.
![image](https://github.com/user-attachments/assets/130a4ae4-2e2e-4a35-ae73-dfc647529978)

---------------------------------------------------------------------------------------------------------
