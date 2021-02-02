from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Video


class VideoCreateForm(ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'video', 'preview')
