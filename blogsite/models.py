from django.db import models
from django.http import HttpResponse


class Post(models.Model):
    author = models.ForeignKey("auth.user", on_delete="")
    tittle = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField()
    publication_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     if self.author == "user":
    #         Post.save(self)
    #     else:
    #         HttpResponse("Not authorized")

    def __str__(self):
        return self.tittle


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete="")
    author = models.CharField(max_length=100)
    comment = models.TextField()
    create_date = models.DateTimeField()
    approve = models.BooleanField(default= False)

    def __str__(self):
        return self.author
