from django.db import models

# Create your models here.

class tempschool(models.Model):
    schoolname=models.CharField(max_length=500)
    schoolnumber=models.PositiveBigIntegerField()
    schoolphone=models.PositiveBigIntegerField()
    schoolemail=models.CharField(max_length=500)
    schooladdress=models.CharField(max_length=1000)
    schoolpassword=models.CharField(max_length=8)
    
class permanentschool(models.Model):
    schoolname=models.CharField(max_length=500)
    schoolnumber=models.PositiveBigIntegerField()
    schoolphone=models.PositiveBigIntegerField()
    schoolemail=models.CharField(max_length=500)
    schooladdress=models.CharField(max_length=1000)
    schoolpassword=models.CharField(max_length=8)
    
class studenttempschoolreg(models.Model):
    schoolnumber=models.PositiveBigIntegerField()
    classname=models.CharField(max_length=50)
    studentid=models.PositiveBigIntegerField()
    
class studentpermanentschoolreg(models.Model):
    schoolnumber=models.PositiveBigIntegerField()
    classname=models.CharField(max_length=50)
    studentid=models.PositiveBigIntegerField()
    
    
class studentresult(models.Model):
    studentid=models.PositiveBigIntegerField()
    schoolid=models.PositiveBigIntegerField()
    passingdate=models.DateField(auto_now_add=True,null=True)
    studentclass=models.CharField(max_length=50)
    studentpercentage=models.PositiveBigIntegerField()
    
    