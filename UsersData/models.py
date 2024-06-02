from django.db import models

# Create your models here.

class userInfo(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    DOB = models.DateField()