import datetime
from django.db import models



class Student(models.Model):
    UUID = models.IntegerField(default=0)
    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    rating = models.IntegerField(default=0)

class Tutor(models.Model):
    UUID = models.IntegerField(default=0)
    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    rating = models.IntegerField(default=0)