from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no=models.IntegerField(max_length=20)
    birth_date=models.DateField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    hire_date=models.DateField(max_length=50)