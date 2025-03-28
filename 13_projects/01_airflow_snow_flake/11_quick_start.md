1. Start EC2 instance
2. Connect to it using putty</br>
    login as: `ubuntu`
    ```python
    source venv/bin/activate
    
    airflow db init
    airflow webserver
    ```
   Let's update the session time
   ![image](https://github.com/user-attachments/assets/ac976f08-bb51-46cc-8b57-bdac4cd16b41)

3. Duplicate the putty session
    login as: `ubuntu`
    ```python
    source venv/bin/activate
    
    airflow scheduler
    ```
4. Airflow runs on 8080 by default.</br>
   So, it will be running at `http://3.236.162.127:8080`, where the IP address is EC2 IP address.</br>
   Username: `airflow`</br>
   Password: `admin@123!`
