from django.db import models
from martor.models import MartorField


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=7, default="#007bff")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MartorField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
