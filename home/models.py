from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
