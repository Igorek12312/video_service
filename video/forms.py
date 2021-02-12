from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Video, Comment


class VideoCreateForm(ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'video', 'preview')


class VideoUpdateForm(ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'preview')


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
