from django.db import models

# Create your models here.
class Article(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    university = models.CharField(max_length=100)
    adviser = models.CharField(max_length=50)
    article = models.CharField(max_length=50)
    about = models.TextField()