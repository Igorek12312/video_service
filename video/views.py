from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from .models import Video
from .forms import VideoCreateForm


class VideoDetailView(DetailView):
    template_name = 'video_page.html'
    model = Video


class VideoListView(ListView):
    model = Video
    paginate_by = 20
    template_name = 'video_channel.html'


class VideoChannelListView(ListView):
    paginate_by = 20
    template_name = 'video_channel.html'

    def get_queryset(self):
        self.author = self.kwargs['username']
        return Video.objects.filter(author__username=self.author).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context

# сделать проверку авторизации
class VideoCreateView(CreateView):
    template_name = 'add_video.html'
    model = Video
    form_class = VideoCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect('/')  # сделать перенаправление на канал пользователя


class VideoDeleteView(DeleteView):
    pass
