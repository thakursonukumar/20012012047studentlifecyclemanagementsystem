from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class hods(models.Model):
    email=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=8)
    
class staff(models.Model):
    name=models.CharField(max_length=50)
    phone=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=8)
    adhar=models.PositiveBigIntegerField()
    email=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=8)
    dob=models.DateField(auto_now_add=True,null=True)
    address=models.CharField(max_length=200)
    