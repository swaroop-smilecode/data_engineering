##### What is back filling?
- As Airflow allows us to define schedule intervals from an arbitrary start date,</br> 
  we can also define past intervals from a start date in the past.
- This behavior is controlled by DAG `catchup` parameter.</br>
  By default, it's fasle, hence back filling is enabled.</br>
  
