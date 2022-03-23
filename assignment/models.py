from dataclasses import field
from email.policy import default
from importlib import resources
from django.db import models

# Create your models here.

class Survivors(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=50)
    gender = models.CharField(max_length=50)
    last_location = models.JSONField()
    infected = models.IntegerField(default=0)
    resources = models.JSONField(default=None)


    class META:
        fields = '__all__'

   
