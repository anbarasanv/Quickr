from django.db import models
from datetime import date

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_code = models.CharField(max_length=20,primary_key=True)
    department = models.CharField(max_length=30)
    score = models.IntegerField()
    created_date = models.DateField(default=date.today)

    class Meta:
        db_table = "employee"
