from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

class UserFile(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    time_registered = models.DateTimeField(default= timezone.now)
