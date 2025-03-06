![image](https://github.com/user-attachments/assets/0ab931a9-4be5-4c52-b426-f40ab6a0f16d)

#### Operator:
In Airflow, operators have a single piece of responsibility: they exist to perform one single piece of work.</br>
The role of a DAG is to orchestrate the execution of a collection of operators.</br>
Examples</br>
- BashOperator (used to run a Bash script)
- PythonOperator (used to run a Python function)
- EmailOperator (used to send an email)
- SimpleHTTPOperator (used to call an HTTP endpoint). Either way, they perform a single piece of work.

#### Note:
In this context & throughout the Airflow documentation, you will see the terms `operator` and `task` used interchangeably.

But, if you want to see exact difference;
Operators provide the implementation of a piece of work, where as Tasks in Airflow manage the execution of an operator.
Taststhey can be thought of as a small wrapper or manager around an operator that ensures the operator executes correctly.
