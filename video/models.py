import os
from django.db import models
from django.contrib.auth.models import User
from video_service import settings


class Video(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE, db_index=True)
    video = models.FileField(upload_to="video")
    preview = models.ImageField(upload_to='preview', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.video.name))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.preview.name))
        super().delete(*args, **kwargs)


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE, db_index=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, db_index=True)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
