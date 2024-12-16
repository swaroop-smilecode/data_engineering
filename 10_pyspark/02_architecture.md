![image](https://github.com/user-attachments/assets/4521a0a4-4d35-4788-97fb-8faa6d818a09)
#### Spark Applications 
Spark Applications consist of a driver process and a set of executor processes.</br>

<ins>Driver Process:</ins></br> 
The driver process runs your main() function, sits on a node in the cluster, and is responsible for three things.
1. Maintaining information about the Spark Application
2. Responding to a user’s program or input
3. Analyzing, distributing, and scheduling work across the executors

<ins>Executor Processes:</ins></br>
The executors are responsible for actually carrying out the work that the driver assigns them.
1. Executing code assigned to it by the driver
2. Reporting the state of the computation on that executor back to the driver node.
Spark, in addition to its cluster mode, also has a local mode. Which means that all the executors can live on the same machine.</br>
In local mode, the driver and executurs run (as threads) on your individual computer instead of a cluster.
