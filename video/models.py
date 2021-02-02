import datetime
from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE, db_index=True)
    video = models.FileField(upload_to="video")
    preview = models.ImageField(upload_to='preview', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
