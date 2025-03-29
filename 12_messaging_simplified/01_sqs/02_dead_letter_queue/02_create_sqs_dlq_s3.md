#### Creating SQS & DLQ
As a first step, let's create 2 queues</br>
`sourceQueue`</br>
`dlqQueue`

Very important point to understand here is: There is no such queue named DLQ separately in AWS.</br>
It's an concept. DLQ is nothing but an regular queue, but the purpose for which that queue used is different,</br>
Hence named DLQ.
