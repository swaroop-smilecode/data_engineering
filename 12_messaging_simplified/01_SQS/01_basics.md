#### What is SQS?
Fully managed message queuing system.

#### What's the need of it?
Let's consider `System A` is sending 1000 requests/sec, but lambda which processes those requests is capable of processing 1 request/sec.</br>
That's why a queue is needed in middle to store these messages. It's lambda duty to poll for new message when it's ready to process.
![image](https://github.com/user-attachments/assets/9340bd53-d8e5-43bf-8e6a-30e943244681)

#### Architecture
`System A` : Producer</br>
`lambda` : Consumer
![image](https://github.com/user-attachments/assets/1b04c88f-8db1-4584-b2ff-03e9722f059a)

-----------------------------------------------------------------------------------------
Let's consider `System A` stores messages into `SQS`</br>
On the other side of the coin, Multiple consumers keep polling for the message.</br>
Who ever get's it first, they start processing & during that time, message will not be visible to other consumers. Why?</br>
Why do you want same message to be processed by multilpe AWS services? That's not the purpose of SQS</br>
And finally, once the message is processed successfully, it get's deleted from queue.
![image](https://github.com/user-attachments/assets/30638ade-3ca5-4d35-bf92-9d27f2f41f4b)
