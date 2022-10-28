from contextlib import nullcontext
from email.policy import default
from platform import release
from urllib import request
from django.db import models

class Cells(models.Model):
    # rto=models.ForeignKey(Rto,on_delete=models.CASCADE)
    cellno=models.CharField(max_length=100)
    capacity=models.CharField(max_length=100)

class Designation(models.Model):
    # rto=models.ForeignKey(Rto,on_delete=models.CASCADE)
    designation=models.CharField(max_length=100)

class Prisoner(models.Model):
    # rto=models.ForeignKey(Rto,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    height=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    photo=models.FileField()

class Police(models.Model):
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    
class Crime(models.Model):
    prisoner=models.ForeignKey(Prisoner,on_delete=models.CASCADE)
    cellno=models.ForeignKey(Cells,on_delete=models.CASCADE)
    crimetitle=models.CharField(max_length=100,default=0)
    crimedetails=models.CharField(max_length=500,default=0)
    crimedate=models.DateField()
    crimetime=models.CharField(max_length=100)
    hearingdate=models.DateField()
    punishment=models.CharField(max_length=100)    
    crimestatus=models.CharField(max_length=100)    

class Visitor(models.Model):
    prisoner=models.ForeignKey(Prisoner,on_delete=models.CASCADE)
    vdate=models.DateTimeField()    
    visitorname=models.CharField(max_length=100)
    relation=models.CharField(max_length=100)    
    purpose=models.CharField(max_length=100) 
    carry=models.CharField(max_length=100) 
    status=models.CharField(max_length=100) 

class InOut(models.Model):
    prisoner=models.ForeignKey(Prisoner,on_delete=models.CASCADE)
    outdatetime=models.DateTimeField(null=True)
    indatetime=models.DateTimeField(null=True)
    reason=models.CharField(max_length=100) 
    status=models.CharField(max_length=100)    

class Parole(models.Model):
    prisoner=models.ForeignKey(Prisoner,on_delete=models.CASCADE)
    pdate=models.DateField()
    days=models.IntegerField()

class Release(models.Model):
    prisoner=models.ForeignKey(Prisoner,on_delete=models.CASCADE)
    reldate=models.DateField()
    
class Finance(models.Model):
    release=models.ForeignKey(Release,on_delete=models.CASCADE)
    amount=models.BigIntegerField()