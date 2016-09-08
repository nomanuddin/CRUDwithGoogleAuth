from django.db import models
from django.contrib.auth.models import User
import os

class userdata(models.Model):
    first_name =  models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    iban = models.CharField(max_length=40)