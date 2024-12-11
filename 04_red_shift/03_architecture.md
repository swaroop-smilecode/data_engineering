#### Architecture
![image](https://github.com/user-attachments/assets/bde0f672-ddbc-4273-a448-3b0edfc7dd32)

- Just remember the word, Massively parallel processing.
- When a query comes to redshift cluster, master node prepares the execution plan.
- When you are creating redshift cluster, it will ask you, do you need child nodes to be `dense compute nodes` / `dense storage nodes`.</br>
  With these options, there is no possibility of scaling compute power & storage power independently.</br>
  To over come this, AWS came up with new child node type named `RA3 node`. It's recommended to select this option.</br>
