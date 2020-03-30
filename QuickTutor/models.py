import datetime
import uuid 
from django.db import models
import random


class Student(models.Model):
    email = models.CharField(max_length=100, default='', primary_key=True)
    username = models.CharField(max_length=10, default='')

    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    
    rating = models.IntegerField(default=0)

#     matchedID = models.UUIDField(default=0, editable=True)
    status = models.IntegerField(default=0)     # 0=canceled/off        1=waiting           2=accepted
    disabled = models.IntegerField(default=0)   # 0=not disabled        1=disabled
    accepted = models.IntegerField(default=0)

class StudentRequest(models.Model):
     # form information
     #courseName = models.OneToOneField(Course, on_delete=models.CASCADE)
     header = models.CharField(max_length=100, default='')
     description = models.CharField(max_length=1000, default='')
     courseName = models.CharField(max_length=100, default='')
     location = models.CharField(max_length=100, default='')
     meetingDetails = models.CharField(max_length=1000, default='')
     confusionMeter = models.IntegerField(default=0)  

     # student ID
     studentEmail = models.CharField(max_length=100, default='')
     studentUsername = models.CharField(max_length=10, default='')
    #commenting out the below for now
     #tutorEmail = models.CharField(max_length=100, default='')
     #tutorUsername = models.CharField(max_length=10, default='')

class Tutor(models.Model):
    email = models.CharField(max_length=100, default='', primary_key=True)
    username = models.CharField(max_length=10, default='')

    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    
    rating = models.IntegerField(default=0)
#     matchedID = models.UUIDField(default=0, editable=True)
    status = models.IntegerField(default=0)     # 0=canceled/off        1=waiting           2=accepted
    disabled = models.IntegerField(default=0)   # 0=not disabled        1=disabled
    request = models.ForeignKey(StudentRequest, on_delete=models.CASCADE, default='', blank=True, null=True)

class TutorCourse(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='tutor')
    course = models.CharField(max_length=100, default='')
    
    


#class RequestCourse(models.Model):
 #   request = models.OneToOneField(StudentRequest, on_delete=models.CASCADE, related_name='request')
  #  course = models.CharField(max_length=100, default='')

