# Quickr

Bellow endpoint will show the employees data orderd by score and descending order:

http://127.0.0.1:8000/employees/


Bellow endpoint will accept a query perameter "chunk" will return the response as 20-employe objects chunk:

http://127.0.0.1:8000/employees/?chunk=3


Note:

Table Structure:

#table_name: employee

#fields:

employee_code => CharField(max_length=20,primary_key=True)
department =>  CharField(max_length=30)
score => IntegerField()
created_date =>  DateField(default=date.today)
