#### Topic
- Producers publish messages to topic.
- Consumers subscribe to topic, to consume those messages.
#### Topic partition
- It's an list associated to topic.
  ![image](https://github.com/user-attachments/assets/dd71ac16-df5b-4d18-904b-e1e489b5275b)
- Topic is just name given to group of partitions. Actual message sent by the producer is stored inside partition.
  ![image](https://github.com/user-attachments/assets/3b000061-b583-4aae-b8e5-d5725a150713)
- New messages are appended at the end.
  `Look now. I told that, kafka is nothing but a queue behind the scences, right?`</br>
  `Are you relating that sentence now?`
- Message stored inside the partition is immutable.
