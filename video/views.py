from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Video
from .forms import VideoCreateForm


class VideoDetailView(DetailView):
    template_name = 'video_page.html'
    model = Video


class VideoListView(ListView):
    model = Video
    paginate_by = 20
    template_name = 'main.html'
    ordering = '-created_at'


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


class VideoCreateView(CreateView):
    template_name = 'add_video.html'
    model = Video
    form_class = VideoCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(f'/{self.request.user}')


class VideoDeleteView(DeleteView):
    model = Video
    template_name = "video_confirm_delete.html"

    def get_object(self, queryset=None):
        obj = super(VideoDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse('video_channel', kwargs={'username': self.request.user})


class VideoUpdateView(UpdateView):
    pass
