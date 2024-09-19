from django.shortcuts import render

# music/views.py
from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer

class MusicListCreate(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
