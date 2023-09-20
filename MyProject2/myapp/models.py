from django.db import models

# Create your models here.

class Student1(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
