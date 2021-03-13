from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Author(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Manga(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, default='0000')
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(default=timezone.now)
    author = models.ManyToManyField(Author)
    ongoing = models.BooleanField(default=True)
    genre = models.ManyToManyField(Genre)
    views = models.IntegerField(default=0)
    total_star = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    thumbnail_url = models.URLField(max_length=200, default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=30)
    num_page = models.IntegerField(default=0)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    cdn_url = models.URLField(max_length=200, default=None)
    code = models.CharField(max_length=30, default=None, unique=False, null=True)
    last_updated = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name + ' of ' + self.manga.name
    
