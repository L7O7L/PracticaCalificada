from pyexpat import model
from django.db import models
from django import forms
# Create your models here.

class user(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


