import datetime
import uuid 
from django.db import models
import random
import os
from datetime import datetime, date, time, timezone, timedelta

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.username), filename)

class Student(models.Model):
    email = models.CharField(max_length=100, default='', primary_key=True)
    username = models.CharField(max_length=100, default='')
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    
    rating = models.IntegerField(default=0)
    numOfRatings = models.IntegerField(default=0)

#     matchedID = models.UUIDField(default=0, editable=True)
    status = models.IntegerField(default=0)     # 0=canceled/off        1=waiting           2=accepted
    disabled = models.IntegerField(default=0)   # 0=not disabled        1=disabled
    accepted = models.IntegerField(default=0)

    balance = models.IntegerField(default=1000)    # in USD

class StudentRequest(models.Model):
    # form information
    #courseName = models.OneToOneField(Course, on_delete=models.CASCADE)

    header = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=1000, default='')
    courseName = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    meetingDetails = models.CharField(max_length=1000, default='')
    confusionMeter = models.IntegerField(default=0)  
    requestTime = models.TimeField(auto_now=False, auto_now_add=False, default = datetime.now())
    
    # student ID
    studentEmail = models.CharField(max_length=100, default='')
    studentUsername = models.CharField(max_length=10, default='')

    #note that these will be used differently, now to store only the tutor that the student chooses!
    tutorEmail = models.CharField(max_length=100, default='')
    tutorUsername = models.CharField(max_length=10, default='')
    
    # session status
    status = models.IntegerField(default=0, null=True)     # 0=not started        1=started  

    sessionStartTime = models.TimeField(auto_now=False, auto_now_add=False, default = datetime.now())
    sessionElapsedTime = models.DurationField(default = timedelta())
    sessionEndTime = models.TimeField(auto_now=False, auto_now_add=False, default = datetime.now())
    sessionEnded = models.IntegerField(default=0, null=True)    # 0=not ended   1=ended
    deleteStatus = models.IntegerField(default=0)   # 0=no one submitted postsession        # 1=one submitted       #2=all submitted, delete row

class Tutor(models.Model):
    email = models.CharField(max_length=100, default='', primary_key=True)
    username = models.CharField(max_length=100, default='')
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    
    rating = models.IntegerField(default=0)
    numOfRatings = models.IntegerField(default=0) 

#     matchedID = models.UUIDField(default=0, editable=True)
    status = models.IntegerField(default=0)     # 0=canceled/waiting/off        2=accepted by student
    disabled = models.IntegerField(default=0)   # 0=not disabled                1=disabled
    request = models.ForeignKey(StudentRequest, on_delete=models.SET_NULL, default=None, null=True)

    balance = models.IntegerField(default=0)    # in USD

class TutorCourse(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    course = models.CharField(max_length=100, default='')
    
class Complaint(models.Model):
    complainantUsername = models.CharField(max_length=10, default='')
    complaineeUsername = models.CharField(max_length=10, default='')
    description = models.CharField(max_length=1000, default='')

class Message(models.Model):
     senderEmail = models.CharField(max_length=100, default='')
     recieverEmail = models.CharField(max_length=100, default='')
     msg_content = models.CharField(max_length=1000, default='')
     created_at = models.TimeField(auto_now_add=True)
