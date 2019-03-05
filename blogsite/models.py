from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete="")
    tittle = models.CharField(max_length=100)
    text = models.TextField()
    publication_day = models.DateTimeField()

    def __str__(self):
        return self.author


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete="")
    author = models.CharField()
    text = models.TextField()
    create_date = models.DateTimeField()
    approve_date = models.DateTimeField()

    def __str__(self):
        return self.post
