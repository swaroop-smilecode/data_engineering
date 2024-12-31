```python
sudo su
cd ~
```
----------------------------------------------------
Observe the volumes you are creating related to jupyter notebook container
```python
volumes:
  - ./jupyter_notebook_files:/home/jovyan/jupyter_notebook_files
  - ./data:/home/jovyan/data
```

This docker compose file is going to create an user named jovyan in the host machine & that guy won't have access to the folders named `jupyter_notebook_files` 
& `data` that are created above.
In order to provide the permisssion to jovyan user, execute the below command in your host machine(linux).
```python
sudo chown -R 1000:1000 /root/pyspark_simple_end_to_end_project
```
----------------------------------------------------
```python
service docker start
cd pyspark_simple_end_to_end_project
docker-compose up
```

----------------------------------------------------

```python
http://3.230.163.119:8888
http://3.230.163.119:4040
```
