from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Manga(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    last_updated = models.DateTimeField()

    