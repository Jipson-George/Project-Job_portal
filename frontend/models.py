from django.db import models

# Create your models here.

class applicantregdb(models.Model):
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=100)
    status=models.CharField(max_length=100,default="ok")

class applicantprofiledb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to='Applicants',null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Street=models.CharField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Nation=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=100,null=True,blank=True)
    Ddate=models.CharField(max_length=100,null=True,blank=True)
    Dmonth=models.CharField(max_length=100,null=True,blank=True)
    Dyear=models.CharField(max_length=100,null=True,blank=True)
    Marital=models.CharField(max_length=100,null=True,blank=True)
    Pg=models.CharField(max_length=100,null=True,blank=True)
    Inst1=models.CharField(max_length=100,null=True,blank=True)
    Degree=models.CharField(max_length=100,null=True,blank=True)
    Inst2=models.CharField(max_length=100,null=True,blank=True)
    Tenth=models.CharField(max_length=100,null=True,blank=True)
    Inst3=models.CharField(max_length=100,null=True,blank=True)
    Others=models.CharField(max_length=100,null=True,blank=True)
    Inst4=models.CharField(max_length=100,null=True,blank=True)
    Skill1=models.CharField(max_length=100,null=True,blank=True)
    Skill2=models.CharField(max_length=100,null=True,blank=True)
    Skill3=models.CharField(max_length=100,null=True,blank=True)
    Exp=models.CharField(max_length=100,null=True,blank=True)
    Exp2=models.CharField(max_length=100,null=True,blank=True)
    Exp3=models.CharField(max_length=100,null=True,blank=True)

    Date=models.DateTimeField(auto_now_add=True)
    Resume=models.FileField(upload_to='resumes',null=True,blank=True)
    Des1=models.CharField(max_length=100,null=True,blank=True)
    Des2=models.CharField(max_length=100,null=True,blank=True)
    Des3=models.CharField(max_length=100,null=True,blank=True)
    Score1=models.CharField(max_length=100,null=True,blank=True)
    Score2=models.CharField(max_length=100,null=True,blank=True)
    Score3=models.CharField(max_length=100,null=True,blank=True)
    Score4=models.CharField(max_length=100,null=True,blank=True)

class enquirydb(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=200)