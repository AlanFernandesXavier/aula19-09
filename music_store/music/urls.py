# music/urls.py
from django.urls import path
from .views import MusicListCreate

urlpatterns = [
    path('musics/', MusicListCreate.as_view(), name='music-list-create'),
]
