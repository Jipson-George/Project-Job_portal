from django.db import models

import datetime
# Create your models here.
class Employerregdb(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,null=True,blank=True)

    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=100)

class jobpostdb(models.Model):
    Cid=models.IntegerField(null=True,blank=True)
    empid=models.IntegerField(null=True,blank=True)
    Title=models.CharField(max_length=100)
    User=models.CharField(max_length=100)
    Company=models.CharField(max_length=100)
    Cemail=models.EmailField(max_length=100,null=True,blank=True)
    Type=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Experiance=models.CharField(max_length=100)
    Salary=models.CharField(max_length=100)
    Requirement=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=200)
    Date =models.DateField(auto_now_add=True)
    approval=models.CharField(max_length=100,default="pending")

    website=models.CharField(max_length=100,null=True,blank=True)


class applicationdb(models.Model):
    jobid=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    cover=models.CharField(max_length=200)
    Cemail=models.EmailField(max_length=100,null=True,blank=True)
    Resume=models.FileField(upload_to='applicantresume',null=True,blank=True)
    Date=models.DateField(auto_now_add=True)
class companydb(models.Model):
    Eemail=models.CharField(max_length=200)
    Ename=models.CharField(max_length=200)
    Company=models.CharField(max_length=200)
    Nature=models.CharField(max_length=200)
    Enumber=models.CharField(max_length=200)
    Founded=models.CharField(max_length=200)
    Contact=models.CharField(max_length=200)
    Cemail=models.EmailField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=200)
    Description=models.CharField(max_length=300)
    Logo=models.ImageField(upload_to='Logo',null=True,blank=True)
    Date=models.DateField(auto_now_add=True)
    Documentation=models.FileField(upload_to='Companydoc',null=True,blank=True)
    Website=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,default="Pending")