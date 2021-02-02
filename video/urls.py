from django.urls import path
from .views import VideoDetailView, VideoListView, VideoChannelListView, VideoCreateView

urlpatterns = [
    path('<str:username>', VideoChannelListView.as_view(), name='video_channel'),
    path('video/<int:pk>', VideoDetailView.as_view(), name='video_detail'),
    path('add_video/', VideoCreateView.as_view(), name='add_video'),
    path('', VideoListView.as_view(), name='main_page'),
]