from django.urls import path
from .views import login, logout, registration, edit_user

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('registration/', registration),
    path('edit/', edit_user),
]