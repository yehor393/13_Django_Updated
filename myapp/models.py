from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    quote = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.TextField()

    def __str__(self):
        return self.title