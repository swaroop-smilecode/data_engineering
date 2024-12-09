#### <ins>Note</ins>
`Let's start with note`.</br>
`Athena can't run SQL queries on the data that is present inside the warehouse(For ex: Redshift)`.</br>
`Athena works only on the data present inside S3 bucket`.

#### What is Athena?
- Athena helps you analyze unstructured, semi-structured, and structured data stored in Amazon S3.
- It's server less, similar to lambda service.
![image](https://github.com/user-attachments/assets/9d92215a-3a2e-43e4-a8da-30c95f378d23)

#### The way of Athena working
Amazon s3 can contain unstructured, semi-structured, and structured data.</br>
So, it's really difficult to write an SQL query on top of all this mingled data.</br>
Because if this reason, athena expects an data catalog & if you want to create that catalog using AWS service, then glue is better option.</br>
![image](https://github.com/user-attachments/assets/c2c88596-223e-4e25-89d2-745726276c53)
