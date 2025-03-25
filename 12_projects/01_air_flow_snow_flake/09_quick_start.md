1. Start EC2 instance
2. Connect to it using putty
    login as: `ubuntu`
    ```python
    source venv/bin/activate
    
    airflow db init
    airflow webserver
    ```
   Let's update the session time
   ![image](https://github.com/user-attachments/assets/ac976f08-bb51-46cc-8b57-bdac4cd16b41)

4. Duplicate the putty session
    login as: `ubuntu`
    ```python
    source venv/bin/activate
    
    airflow scheduler
    ```

