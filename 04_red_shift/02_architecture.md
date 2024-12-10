#### Architecture
![image](https://github.com/user-attachments/assets/2d1d35bd-8344-46d3-a8ba-ccdd02ce646e)

- When a query comes to redshift cluster, leader node prepares the execution plan.
- When you are creating redshift cluster, it will ask you, do you need child nodes to be `dense compute nodes` / `dense storage nodes`.</br>
  With these options, there is no possibility of scaling compute power & storage power independently.</br>
  To over come this, AWS came up with new child node type named `RA3 node`. It's recommended to select this option.</br>

#### Slices
Each slice is allocated a portion of the node's memory and disk space.
![image](https://github.com/user-attachments/assets/74b78162-f5cc-49c4-a13b-a72fd95b147a)
