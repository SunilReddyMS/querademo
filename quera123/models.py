from django.db import models

# Create your models here.

class signup(models.Model):
    user=models.CharField(max_length=50)
    passwd=models.CharField(max_length=50)
