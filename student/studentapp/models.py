from django.db import models

# Create your models here.

class stud(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=10)
