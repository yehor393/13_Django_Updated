from django.db import models
from myapp.models import Post

class Authors(models.Model):
    name = models.CharField(unique=True, max_length=50)
    post = models.ManyToManyField(Post)