from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Technologies(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'images')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False) 
