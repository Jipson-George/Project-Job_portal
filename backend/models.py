from django.db import models

# Create your models here.
class jobdb(models.Model):
    jobcat=models.CharField(max_length=100,null=True,blank=True)
class job_typedb(models.Model):
    jobtype=models.CharField(max_length=100)

class verifiedjobdb(models.Model):
    Jobid=models.IntegerField(null=True,blank=True)
    Title = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Experiance = models.CharField(max_length=100)
    Salary = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Date = models.DateField(auto_now_add=True)
    approval=models.CharField(max_length=100,default="verified")
    Requirement=models.CharField(max_length=100,null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)
    Cemail=models.CharField(max_length=100,null=True,blank=True)

    # logo=models.ImageField(upload_to='Verifiedlogo',null=True,blank=True)



















