from django.db import models

# Create your models here.

class StudentData1(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    mobile=models.IntegerField()
    marks1=models.IntegerField()
    marks2=models.IntegerField()
    marks3=models.IntegerField()
    marks4=models.IntegerField()
    