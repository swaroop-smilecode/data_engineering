- There is an application named `register_user_application`, whose duty is to enable users to get registerted.</br>
  Once a new user is registered, his details are published to kafka server to a topic named `users`.</br>
- kafka cluster takes those messages & broadcasts them.
- On the other side of coin, there is another application(data analysis) whose duty is to analyze below insights about user details.</br>
  This is the consumer application which is subscribed to topic named `users`.</br>
  1. How many users are registered as of now?</br>
  2. Show the users data/each year.</br>
  
![image](https://github.com/user-attachments/assets/1ef3a52c-f518-4708-8824-ac8dd7abe647)
