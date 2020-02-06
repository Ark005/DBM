from django.db import models

# Create your models here.

class Person (models.Model):
    login = models.CharField (max_length=50,unique= True)
    password = models.CharField (max_length=50)
    name = models.CharField (max_length=50)
    email = models.CharField (max_length=50)