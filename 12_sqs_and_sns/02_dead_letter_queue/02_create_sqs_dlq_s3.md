#### Create SQS & DLQ
As a first step, let's create 2 queues</br>
`sourceQueue`</br>
`dlqQueue`

Very important point to understand here is: There is no such queue named DLQ separately in AWS.</br>
It's an concept. DLQ is nothing but an regular queue, but the purpose for which that queue used is different,</br>
Hence named DLQ.

#### Create s3 bucket
- Create s3 bucket named `redrivepurge`
- Create folder named `unprocessedmessages`.
- Note:
  `s3_prefix_stage` : As per convention, this property is used to represent path upto `bucket_name/folder_name`</br>
  `s3_key` : As per convention, this property is used to represent path upto `bucket_name/folder_name/<another_folder_name>/<file_name.json>`
