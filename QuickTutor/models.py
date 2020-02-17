import datetime
import uuid 
from django.db import models
import random

def genUUID():
     return random.randint(1000000, 10000000)

class Student(models.Model):
    ID = models.IntegerField(default=genUUID(), primary_key=True) 

    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')

    rating = models.IntegerField(default=0)

#     matchedID = models.UUIDField(default=0, editable=True)
    status = models.IntegerField(default=0)     # 0=canceled/off        1=waiting           2=accepted
    disabled = models.IntegerField(default=0)   # 0=not disabled        1=disabled

class Tutor(models.Model):
    ID = models.IntegerField(default=genUUID(), primary_key=True) 

    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')

    rating = models.IntegerField(default=0)
    
#     matchedID = models.UUIDField(default=0, editable=True)
    status = models.IntegerField(default=0)     # 0=canceled/off        1=waiting           2=accepted
    disabled = models.IntegerField(default=0)   # 0=not disabled        1=disabled

class studentRequest(models.Model):
     # form information
     courseName = models.CharField(max_length=100, default='')
     subject = models.CharField(max_length=100, default='')
     description = models.CharField(max_length=100, default='')
     subject = models.CharField(max_length=100, default='')
     location = models.CharField(max_length=100, default='')
     confusionMeter = models.IntegerField(default=0)

     # student ID
     studentID = models.IntegerField(default=0)
     tutorID = models.IntegerField(default=0)

